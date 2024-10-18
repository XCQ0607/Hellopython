import time
from itertools import zip_longest   # 导入 zip_longest 函数，用于处理不同长度的可迭代对象

def demonstrate_loops():
    print("Python3 循环语句示例\n")

    # 1. 基本的 for 循环
    print("1. 基本的 for 循环:")
    for i in range(5):
        print(f"  迭代 {i}")

    # 2. while 循环
    print("\n2. while 循环:")
    count = 0
    while count < 5:
        print(f"  计数: {count}")
        count += 1

    # 3. 遍历列表
    print("\n3. 遍历列表:")
    fruits = ["苹果", "香蕉", "橙子"]
    for fruit in fruits:
        print(f"  水果: {fruit}")

    # 4. 遍历字典
    print("\n4. 遍历字典:")
    person = {"name": "Alice", "age": 30, "city": "New York"}
    for key, value in person.items():
        print(f"  {key}: {value}")

    # 5. enumerate() 函数     # 同时获取索引和值`
    print("\n5. 使用 enumerate():")
    for index, fruit in enumerate(fruits):
        print(f"  索引 {index}: {fruit}")

    # 6. zip() 函数   # 同时遍历多个可迭代对象
    print("\n6. 使用 zip():")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"  {name} 是 {age} 岁")

    # 7. 列表推导式
    print("\n7. 列表推导式:")
    squares = [x**2 for x in range(5)]
    print(f"  平方数: {squares}")

    # 8. 带条件的列表推导式
    print("\n8. 带条件的列表推导式:")
    even_squares = [x**2 for x in range(10) if x % 2 == 0]  #三元运算
    print(f"  偶数的平方: {even_squares}")

    # 9. 嵌套循环
    print("\n9. 嵌套循环:")
    for i in range(3):
        for j in range(3):
            print(f"  ({i}, {j})", end=" ")
        print()  # 换行

    # 10. break 语句
    print("\n10. 使用 break:")
    for i in range(10):
        if i == 5:
            break
        print(f"  {i}", end=" ")
    print("\n  循环在 5 处中断")

    # 11. continue 语句
    print("\n11. 使用 continue:")
    for i in range(5):
        if i == 2:
            continue
        print(f"  {i}", end=" ")
    print("\n  跳过了 2")

    # 12. else 子句
    print("\n12. 循环的 else 子句:")
    for i in range(5):
        print(f"  {i}", end=" ")
    else:     # 循环正常完成时执行，如果循环被 break 中断，则不执行
        print("\n  循环正常完成")

    # 13. pass 语句
    print("\n13. 使用 pass:")
    for i in range(3):
        if i == 1:
            pass  # 不做任何事，用于占位，与continue相比，continue是跳过当前循环，pass是不做任何事，继续执行下一行代码，相当于无用。
            print(f"当i等于{i}可以执行", end=" ")
        else:
            print(f"  {i}", end=" ")
    print("\n  pass 用于占位")

    # 14. 反向循环
    print("\n14. 反向循环:")
    for i in reversed(range(5)):    #记住.reserve()函数，list/tuple/set/dict等都可以使用.reserve()函数
        print(f"  {i}", end=" ")
    print()

    # 15. 无限循环
    print("\n15. 无限循环 (会在3秒后中断):")
    start_time = time.time()
    while True:
        print("  循环中...", end="\r")  # \r是回车符，将光标移动到行首，这样可以实现覆盖式输出，而不是换行输出，这样可以实现循环中的动态效果。
        if time.time() - start_time > 3:    #time.time()函数返回当前时间的时间戳（时间戳组成： 1970年1月1日0时0分0秒到现在的秒数）
            break
    print("  循环结束")

    # 16. 循环中的异常处理
    print("\n16. 循环中的异常处理:")
    numbers = [1, 2, 0, 4, 5]
    for num in numbers:
        try:
            result = 10 / num
            print(f"  10 / {num} = {result}")
        except ZeroDivisionError:     # 捕获除以零的异常，捕获全部异常使用Exception，Exception是所有异常的父类
            print(f"  无法除以零")

    # 17. 使用 zip_longest()  # 处理不同长度的可迭代对象
    print("\n17. 使用 zip_longest():")
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c', 'd']
    for item1, item2 in zip_longest(list1, list2, fillvalue=None):    # fillvalue=None表示如果两个可迭代对象的长度不同，用None填充
        print(f"  {item1} - {item2}")
    for item2, item1 in zip_longest(list1, list2, fillvalue=None):
        print(f"  {item1} - {item2}")

    # 18. 循环展开
    print("\n18. 循环展开技巧:")
    data = [1, 2, 3, 4, 5, 6, 7]
    for i in range(0, len(data), 3):    #这个range会输出0,3,6
        chunk = data[i:i+3]     #当i+3超出data的长度时，会自动截取到data的末尾
        print(f"  处理块: {chunk}")

if __name__ == "__main__":
    demonstrate_loops()