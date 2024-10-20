from functools import reduce


def main():
    # 1. 基本lambda函数使用   解释格式：  lambda 参数列表: 表达式
    print("1. 基本lambda函数:")
    basic_lambda = lambda x, y: x ** y
    print(f"2^3 = {basic_lambda(2, 3)}")

    # 2. 与map()结合使用     map结合解释格式：  map(函数, 可迭代对象)
    print("\n2. 与map()结合:")
    numbers = [1, 2, 3, 4, 5]
    squared = map(lambda x: x ** 2, numbers)  # map函数的第一个参数是函数，第二个参数是可迭代对象
    print(f"Original: {numbers}")
    print(type(squared))
    print(f"Squared: {list(squared)}")

    # 3. 与filter()结合使用        filter结合解释格式：  filter(函数, 可迭代对象)
    print("\n3. 与filter()结合:")
    even_numbers = filter(lambda x: x % 2 == 0,
                          numbers)  # filter函数与map函数的区别在于，filter函数的返回值是一个迭代器，迭代器中的元素是可迭代对象中的元素，这些元素满足函数的条件
    print(f"Original: {numbers}")
    print(type(even_numbers))
    print(f"Even numbers: {list(even_numbers)}")

    # 4. 与reduce()结合使用        reduce结合解释格式：  reduce(函数, 可迭代对象)
    print("\n4. 与reduce()结合:")
    product = reduce(lambda x, y: x * y,
                     numbers)  # reduce函数的工作原理：先将可迭代对象中的前两个元素作为参数传入函数，然后将函数的返回值与第三个元素作为参数传入函数，以此类推，直到可迭代对象中的所有元素都被传入函数
    print(f"Original: {numbers}")
    print(f"Product: {product}")

    # 5. 与sorted()结合使用
    print("\n5. 与sorted()结合:")
    students = [
        {'name': 'Alice', 'grade': 88},
        {'name': 'Bob', 'grade': 75},
        {'name': 'Charlie', 'grade': 93}
    ]  # 这里的s代表从students中取出一个元素，：后面的代表对该students元素的操作，这里是提取每个元素中的grade键对应的值
    sorted_students = sorted(students, key=lambda s: s['grade'],
                             reverse=True)  # 这里s: s['grade']表示从每个学生的字典中提取grade键对应的值,前面的s是一个元素，后面的s['grade']表示从每个学生的字典中提取grade键对应的值
    # key：一个函数，用来指定排序的规则。默认情况下，sorted函数按照元素的大小进行排序。如果指定了key参数，则会根据key函数的返回值来排序。
    print("Sorted students by grade (descending):")
    for student in sorted_students:
        print(f"{student['name']}: {student['grade']}")
        sorted
    # 函数被用来对一个包含学生信息的列表进行排序。key参数被设置为一个lambda 函数 lambda s: s['grade']，这个函数从每个学生的字典中提取grade键对应的值，并根据这些值对学生进行排序。reverse = True参数表示排序的顺序是降序，即成绩最高的学生排在最前面。

    # 6. 在自定义函数中使用lambda
    print("\n6. 在自定义函数中使用lambda:")

    def apply_operation(operation, x, y):  # 这里的operation是一个函数，x和y是函数的参数
        return operation(x, y)

    add = apply_operation(lambda a, b: a + b, 5, 3)
    multiply = apply_operation(lambda a, b: a * b, 5, 3)
    print(f"5 + 3 = {add}")
    print(f"5 * 3 = {multiply}")

    # 7. 使用lambda创建闭包
    print("\n7. 使用lambda创建闭包:")

    def multiplier(n):
        return lambda x: x * n

    double = multiplier(2)  # 这里的double是一个函数，它的参数是x，它的返回值是x*2
    triple = multiplier(3)
    print(f"Double of 5: {double(5)}")
    print(f"Triple of 5: {triple(5)}")
    # double和triple都是闭包，它们分别记住了multiplier函数调用时传入的n值（2和3），并在后续调用时使用这些值。这就是闭包的主要特点：它们可以访问外部作用域中的变量，并且这些变量在函数返回后仍然存在。
    # 在Python中，闭包（Closure）是一种特殊的函数，它可以访问其外部作用域中的变量，即使这些变量在函数返回后仍然存在。闭包通常是由一个函数和它所引用的外部变量组成的。multiplier函数是一个闭包，因为它返回了一个内部的lambda函数，这个lambda函数可以访问外部的n变量。当你调用multiplier(2)或multiplier(3)时，它返回的lambda函数会记住传入的n值，并在后续调用时使用这个值

    # 8. 带条件的lambda函数
    print("\n8. 带条件的lambda函数:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_or_even = lambda x: 'odd' if x % 2 else 'even'  #if在这里的专业术语是条件表达式，它的格式是：if 条件 else 条件为假时的返回值
    result = list(map(odd_or_even, numbers))
    print(f"Numbers: {numbers}")
    print(f"Odd or Even: {result}")

    # 9. 复合lambda函数
    print("\n9. 复合lambda函数:")
    compose = lambda f, g: lambda x: f(g(x))     #第一个lamdba接受f，g函数，：后进行处理，处理方法是lambda函数，x是对f，g操作的结果返回第一个lambda函数，最后返回compose函数
    square = lambda x: x ** 2
    add_one = lambda x: x + 1
    #f(g(x)) = 函数在这里指的是对传入的x先平方，再对其加一
    square_then_add_one = compose(add_one, square)
    print(f"f(g(3)) where f(x)=x+1 and g(x)=x^2: {square_then_add_one(3)}")

    # 10. 在列表推导式中使用lambda
    print("\n10. 在列表推导式中使用lambda:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = list(map(lambda x: list(map(lambda y: y, x)), zip(*matrix)))   #zip(*matrix)表示将矩阵的行和列进行转置
    print(f"Original matrix: {matrix}")
    print(f"Transposed matrix: {transposed}")
# zip(*matrix)的结果是一个元组的列表   [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
#map先对(1, 4, 7)进行操作，传给内层map函数x，然后对x进行内层lambda函数的操作，也就是给了占位符y，y:y相当于对y没操作，也就是将(1, 4, 7)传出给了list转化为了列表[1, 4, 7]
# 相当于list(map(lambda x: list(x), zip(*matrix)))

if __name__ == "__main__":
    main()
