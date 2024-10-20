# 自定义迭代器类
class FibonacciIterator:
    def __init__(self, n):             # 初始化迭代器，设置迭代次数
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):                 # __iter__是初始化迭代器的方法，返回迭代器对象本身当被迭代时返回迭代器对象本身(即传入参量为self)
        return self

    def __next__(self):                 # 返回下一个斐波那契数
        if self.count < self.n:
            result = self.b
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration

# 生成器函数
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):             # for _ in range(n)表示循环n次，_表示循环变量，不使用循环变量的值，类似pass
        yield b               # yield是生成器函数的关键字，用于返回一个值给调用者，并暂停函数的执行，等待下一次调用
        a, b = b, a + b            # a, b = b, a + b 表示将a的值赋给b，将a + b的值赋给a
# 1. def fibonacci_generator(n)::定义了-个名为 fibonacci_generator 的函数它接受一个参数 n，表示要生成的裴波那契数列的长度。
# 2.a，b =0，1:初始化两个变量 a和 b，分别赋值为 0 和 1，这是悲波那契数列的前两个数。3.for _ in range(n)::使用一个循环来生成 n个数。-是一个占位符，表示我们不关心循环变量的值，只是需要循环n次。yield a:在循环内部，使用 yield 关键字来生成当前的悲波那契数 a，并将其返回给调用者。yield 会暂停函数的执行，等待下一次调用。
# 3.a，b =b，a +b:在每次循环结束后，更新 a和 b 的值，使得a变为 b，b变为a+b，这是悲波那契数列的递推公式。

# 无限生成器
def infinite_counter():
    i = 1
    while True:
        yield i
        i += 1

# 生成器表达式
squares_gen = (x**2 for x in range(10))

#改写为普通函数
# def squares_gen(n):
#     for x in range(n):
#         yield x**2





# 主函数
def main():
    print("1. 使用自定义迭代器:")
    fib_iter = FibonacciIterator(10)
    print(type(fib_iter))         # <class '__main__.FibonacciIterator'>, 自定义迭代器类返回的是一个迭代器对象。__main__表示当前模块，FibonacciIterator表示自定义迭代器类的名称。
    for num in fib_iter:
        print(num, end=' ')
    print("\n")

    print("2. 使用生成器函数:")
    fib_gen = fibonacci_generator(10)
    print(type(fib_gen))         # <class 'generator'>, 生成器函数返回的是一个生成器对象。
    print(next(fib_gen))
    print("---------")
    for _ in range(2):  #不包含2
        print(next(fib_gen))    # next()函数用于返回生成器对象的下一个值。
    print(list(fib_gen))    # list()函数用于将可迭代对象转换为列表。
    print()
    fib_gen = fibonacci_generator(10)
    # 调用一次生成器函数，返回一个生成器对象。
    # 生成器对象并不会一次性生成所有的值，而是在迭代时逐个生成。
    # 生成器对象是一个迭代器，可以被用于for循环或next()
    # 函数。
    # 生成器对象并不会将所有生成的值存储在某个地方，而是在每次迭代时实时生成。

    print("3. 使用next()函数手动迭代:")
    fib_gen = fibonacci_generator(5)
    try:
        while True:
            print(next(fib_gen), end=' ')
    except StopIteration:        # StopIteration是一个异常类，当迭代器没有更多元素时，会抛出这个异常。
        print("\n迭代结束")
    print()

    print("4. 使用无限生成器(限制输出前5个):")
    counter = infinite_counter()
    for _ in range(5):
        print(next(counter), end=' ')
    print("\n")

    print("5. 使用生成器表达式:")
    for square in squares_gen:
        print(square, end=' ')
    print("\n")

    print("6. 使用send()方法与生成器交互:")
    def interactive_gen():
        while True:
            received = yield        #received = yield 表示将yield表达式的值赋给received变量
            print(f"收到: {received}")

    ig = interactive_gen()
    next(ig)  # 启动生成器, 启动生成器函数，执行到yield语句，暂停函数的执行，等待下一次调用。
    ig.send("Hello")      # 发送数据给生成器函数，将数据赋值给yield表达式，然后继续执行print，在while循环中继续执行，执行到yield语句，暂停函数的执行，等待下一次调用。
    ig.send("World")
    print()

    print("7. 使用close()方法关闭生成器:")
    def closeable_gen():
        try:
            yield "正常运行"
            yield "还在运行"
        finally:
            print("生成器被关闭")

    cg = closeable_gen()
    for _ in range(2):
        print(next(cg))
    # closeable_gen生成器函数中有两个yield 语句，因此在第一次循环中，next(cg)将返回"正常运行"，在第二次循环中，它将返回"还在运行"。在第三次循环中，由于没有更多的yield 语句，next(cg)将抛出StopIteration异常，表示生成器已经耗尽。
    cg.close()
    # 当您调用cg.close()时，它会关闭生成器，这将导致生成器内部的 finally 块执行，打印出"生成器被关闭"。这通常用于释放资源或执行清理操作。
if __name__ == "__main__":
    main()