import math
from collections import namedtuple  # 导入 namedtuple 模块，用于创建命名元组类型

def demonstrate_comprehensions():
    print("Python 推导式示例\n")

    # 1. 列表推导式
    print("1. 列表推导式:")
    # 基本用法
    squares = [x**2 for x in range(10)]
    print(f"  平方数: {squares}")

    # 带条件的列表推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]  #添加限制条件
    print(f"  偶数的平方: {even_squares}")

    # 嵌套列表推导式
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]  #num来自row，row来自matrix，从row中取出num，形成一个列表。row是中间变量
    print(f"  展平的矩阵: {flattened}")

    # 使用函数的列表推导式
    def is_prime(n):    #判断是否为质数
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

# 首先检查输入的数n是否小于2。如果是，则直接返回False，因为质数必须大于1。
# 然后，使用一个循环从2开始到n的平方根（取整加1）进行遍历。这是因为如果n不是质数，那么它一定可以被一个小于或等于其平方根的数整除。
# 在循环中，检查n是否能被当前遍历的数i整除。如果能整除，说明n不是质数，返回False。
# 如果循环结束后没有找到能整除n的数，那么n就是质数，返回True。

    primes = [x for x in range(2, 50) if is_prime(x)]
    print(f"  50以内的质数: {primes}")

    # 2. 字典推导式
    print("\n2. 字典推导式:")
    # 基本用法
    squared_dict = {x: x**2 for x in range(5)}
    print(f"  数字及其平方: {squared_dict}")

    # 条件字典推导式
    even_squared_dict = {x: x**2 for x in range(10) if x % 2 == 0}
    print(f"  偶数及其平方: {even_squared_dict}")

    # 从两个列表创建字典
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    key_value_dict = {k: v for k, v in zip(keys, values)}
    print(f"  从列表创建的字典: {key_value_dict}")

    # 3. 集合推导式
    print("\n3. 集合推导式:")
    # 基本用法
    unique_squares = {x**2 for x in range(-5, 5)}    #集合没有重复的元素
    print(f"  唯一的平方数: {unique_squares}")

    # 条件集合推导式
    vowels = set('aeiou')
    consonants = {char for char in 'abcdefghijklmnopqrstuvwxyz' if char not in vowels}
    print(f"  辅音字母: {consonants}")

    # 4. 生成器表达式（元组推导式）
    print("\n4. 生成器表达式:")
    # 基本用法
    gen = (x**2 for x in range(5))
    print("  生成器对象:", gen)
    print("  生成器内容:", list(gen))

    # 使用生成器表达式节省内存
    sum_of_squares = sum(x**2 for x in range(1000000))
    print(f"  前1,000,000个自然数的平方和: {sum_of_squares}")

    # 5. 高级技巧和组合使用
    print("\n5. 高级技巧和组合使用:")
    # 使用 enumerate
    indexed_chars = {index: char for index, char in enumerate('hello')}
    print(f"  带索引的字符: {indexed_chars}")

    # 条件表达式（三元运算符）在推导式中的使用
    parity = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
    print(f"  奇偶性: {parity}")

    # 使用 namedtuple     # 定义一个命名元组类型
    Point = namedtuple('Point', ['x', 'y'])
    points = [Point(x, y) for x in range(3) for y in range(3)]  # 使用for生成一个包含多个点的列表
    print("  点的列表:")
    for point in points:
        print(f"    ({point.x}, {point.y})")

    # 嵌套的字典推导式
    nested_dict = {outer: {inner: inner * outer for inner in range(1, 4)} for outer in range(1, 4)}
    print(f"  嵌套字典: {nested_dict}")

if __name__ == "__main__":
    demonstrate_comprehensions()