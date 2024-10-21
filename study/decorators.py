import time

# 1. 日志记录装饰器
def logger(func):
    def wrapper(*args, **kwargs):   #两个参数，*args表示可变参数，**kwargs表示关键字参数
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)    # 调用原始函数，执行了greet函数
        print(f"Function {func.__name__} returned: {result}")
        return result    # 返回原始函数的结果

    return wrapper
# 如果在 logger 装饰器的 wrapper 函数中不调用传入的 func，那么 func 中的代码就不会执行，只会执行装饰器中的代码。

# 装饰器函数只需要传入 func 这一个参数
# 在装饰器函数内部，通常会定义一个嵌套函数 wrapper，这个 wrapper 函数会包含额外的代码，比如日志记录、性能分析、参数处理等。wrapper 函数会调用传入的 func 函数，并在调用前后执行一些额外的操作。
# 装饰器函数最后会返回 wrapper 函数，这样当调用被装饰的函数时，实际上是在调用 wrapper 函数，从而执行装饰器中定义的额外操作。

# 在装饰器函数中，wrapper 函数定义了 *args 和 **kwargs 作为参数，这意味着它可以接受任意数量的位置参数和关键字参数。当装饰器被应用到一个函数上时，wrapper 函数会在调用原始函数 func 时，将接收到的所有参数原封不动地传递给 func。
# result = func(*args, **kwargs) 这行代码调用了原始函数 func，并将 *args 和 **kwargs 作为参数传递给它。这里的 * 和 ** 操作符用于解包参数，即将元组 args 和字典 kwargs 中的元素分别作为位置参数和关键字参数传递给 func。这样，无论原始函数 func 需要多少个参数，wrapper 都可以正确地调用它。
# 在你提供的代码示例中，当调用 greet("Alice") 时，"Alice" 作为一个位置参数被传递给 greet 函数。在装饰器内部，wrapper 函数接收到这个参数，并将其作为 args 元组的一部分传递给 func（即原始的 greet 函数）。因此，"Alice" 最终作为参数传递给了原始的 greet 函数


# 2. 性能分析装饰器
def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result    # 返回原始函数的结果

    return wrapper


# 3. 带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))   #控制台输出的结果是：Function wrapper returned: ['Hello, Alice!', 'Hello, Alice!'],而不是将每个装饰器的结果都添加到results列表中，而是将每个装饰器的结果都重新执行一遍
            return results
        return wrapper
    return decorator


# 4. 类装饰器
class DecoratorClass:
    def __init__(self, func):   # 定义了一个构造函数，代码起作用是在类被实例化时被调用
        self.func = func      # 将这个函数存储在实例属性 self.func 中

    def __call__(self, *args, **kwargs):    # __call__ 方法是一个特殊的方法，它允许类的实例像函数一样被调用。当实例被调用时，__call__ 方法会执行一些额外的操作，然后调用存储在 self.func 中的函数
        print(f"Class Decorator: Calling function: {self.func.__name__}")
        result = self.func(*args, **kwargs)   # 调用原始函数，执行了add函数
        print(f"Class Decorator: Function {self.func.__name__} returned: {result}")
        return result


# 使用装饰器示例
@logger  # 使用日志记录装饰器
@time_logger  # 使用性能分析装饰器
@repeat(2)  # 使用带参数的装饰器，重复执行 2 次
def greet(name):
    """打印问候语"""
    return f"Hello, {name}!"


@DecoratorClass  # 使用类装饰器
def add(a, b):
    """返回两个数的和"""
    return a + b

# 当你在一个函数前加上 @logger 装饰器时，它会先执行 @logger 中的代码。装饰器的作用是在不改变原函数代码的情况下，为函数添加额外的功能。


# 调用被装饰的函数
print("--- Calling greet function ---")
greet("Alice")

print("\n--- Calling add function ---")
result = add(5, 10)
print(f"Result of add function: {result}")

# 日志记录装饰器(logger)：这个装饰器在函数被调用时，打印出函数的名称和传入的参数，同时，它会打印出返回的结果。
# 性能分析装饰器(time_logger)：此装饰器用于测量函数执行的时间。它在调用函数前记录开始时间，调用完毕后记录结束时间，并计算两者的差值。
# 带参数的装饰器(repeat)：这个装饰器接收一个整数参数n，在调用被装饰的函数时会重复执行该函数n次。
# 类装饰器(DecoratorClass)：一个类装饰器实现了__call__方法，允许其实例像函数一样被调用。它在调用原始函数前后打印信息。




#打包解包
# 打包和解包是Python中处理可变数量参数的一种方式。打包指的是将多个参数组合成一个元组（tuple）或字典（dictionary），而解包则是将一个元组或字典中的元素拆分出来，分别作为函数的参数。
print("\n---打包解包---")
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# 打包参数
args = (1, 2, 3)
kwargs = {'a': 1, 'b': 2, 'c': 3}

# 解包参数并调用函数
my_function(*args, **kwargs)


# 在Python中，函数的参数可以分为位置参数（positional arguments）和关键字参数（keyword arguments）。位置参数是按照参数在函数定义中的位置来传递的，而关键字参数则是通过参数名来传递的。
print("\n---位置参数和关键字参数---")
# 位置参数示例：
def greet(name, message):
    print(f"Hello, {name}! {message}")

# 使用位置参数调用函数
greet("Alice", "How are you?")

# 使用关键字参数调用函数
greet(message="How are you?", name="Alice")
#相当于：
#message="How are you?"
#name="Alice"
#greet(message, name)


# 魔法方法（Magic Methods）或双下划线方法（Dunder Methods）。这些方法在类定义时可用，它们允许你自定义类的行为，使其更符合你的需求。以下是一些常见的魔法方法：
# __str__和__repr__：用于定义对象的字符串表示形式。__str__用于提供对象的友好字符串表示，通常用于打印对象时。__repr__用于提供对象的详细表示，通常用于调试和开发。
# __len__：用于定义对象的长度。当你对一个对象调用len()函数时，会调用这个方法。
# __add__、__sub__、__mul__、__truediv__等：用于定义对象的算术操作。例如，__add__定义了对象的加法操作。
# __eq__、__ne__、__lt__、__gt__等：用于定义对象的比较操作。例如，__eq__定义了对象的相等性比较。
# __getitem__、__setitem__、__delitem__：用于定义对象的索引操作。例如，__getitem__允许你通过索引访问对象的元素。
# __iter__和__next__：用于定义对象的迭代行为。__iter__返回一个迭代器对象，而__next__定义了迭代器的下一个元素。
# __enter__和__exit__：用于定义上下文管理器。这些方法允许你在使用with语句时自定义对象的进入和退出行为。
# 这些方法只是Python中众多魔法方法的一部分，它们可以帮助你更好地控制和扩展类的行为。当你定义一个类时，你可以根据需要实现这些方法，以使你的类更加灵活和强大。

# __init__ 方法：
# __init__ 方法是一个构造函数，它在类的实例化时被自动调用。
# 这个方法的主要作用是初始化对象的属性，即在创建对象时为其设置初始状态。
# __init__ 方法可以接受参数，这些参数可以在创建对象时传递，用于设置对象的初始属性值。
# 例如：
# class MyClass:
#     def __init__(self, name, age):
#         self.name = name  # 初始化实例属性
#         self.age = age
#
# # 创建对象时传递参数
# obj = MyClass("Alice", 30)
# __call__ 方法：
# __call__ 方法允许类的实例像函数一样被调用。
# 当你在类的实例后面加上一对括号 () 时，就会调用这个方法。
# __call__ 方法可以接受参数，这些参数可以在调用实例时传递。
# 例如：
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, age):
#         print(f"My name is {self.name} and I am {age} years old.")
#
# # 创建对象
# obj = MyClass("Alice")
#
# # 调用对象，就像调用函数一样
# obj(30)