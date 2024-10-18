import random

def demonstrate_conditional_control():
    print("Python 条件控制示例\n")

    # 1. 基本的 if-elif-else 结构
    def check_number(num):
        print(f"\n1. 检查数字 {num}:")
        if num > 0:
            print("  正数")
        elif num < 0:
            print("  负数")
        else:
            print("  零")

    check_number(5)
    check_number(-3)
    check_number(0)

    # 2. 比较运算符
    def compare_numbers(a, b):
        print(f"\n2. 比较 {a} 和 {b}:")
        if a > b:
            print(f"  {a} 大于 {b}")
        elif a < b:
            print(f"  {a} 小于 {b}")
        else:
            print(f"  {a} 等于 {b}")

    compare_numbers(10, 5)
    compare_numbers(5, 10)
    compare_numbers(7, 7)

    # 3. 逻辑运算符
    def check_range(num, start, end):
        print(f"\n3. 检查 {num} 是否在 {start} 和 {end} 之间:")
        if start <= num <= end:
            print(f"  {num} 在范围内")
        else:
            print(f"  {num} 不在范围内")

    check_range(15, 10, 20)
    check_range(25, 10, 20)

    # 4. 嵌套的 if 语句
    def categorize_number(num):
        print(f"\n4. 分类数字 {num}:")
        if num % 2 == 0:
            if num > 0:
                print("  正偶数")
            elif num < 0:
                print("  负偶数")
            else:
                print("  零（偶数）")
        else:
            if num > 0:
                print("  正奇数")
            else:
                print("  负奇数")

    categorize_number(4)
    categorize_number(-3)
    categorize_number(0)

    # 5. 三元运算符
    def is_adult(age):
        result = "成年" if age >= 18 else "未成年"
        print(f"\n5. 年龄 {age}: {result}")

    is_adult(20)
    is_adult(15)

    # 6. 使用 'in' 操作符
    def check_fruit(fruit):
        fruits = ["苹果", "香蕉", "橙子"]
        result = "在列表中" if fruit in fruits else "不在列表中"
        print(f"\n6. 水果 '{fruit}' {result}")

    check_fruit("香蕉")
    check_fruit("葡萄")

    # 7. 复杂条件示例
    def evaluate_student(name, score, attendance):
        print(f"\n7. 评估学生 {name}:")
        if score >= 60 and attendance >= 80:
            if score >= 90:
                print("  优秀学生")
            elif score >= 75:
                print("  良好学生")
            else:
                print("  及格学生")
        elif score >= 60 or attendance >= 80:
            print("  需要改进")
        else:
            print("  不及格")

    evaluate_student("Alice", 85, 90)
    evaluate_student("Bob", 55, 95)
    evaluate_student("Charlie", 40, 60)

    # 8. 使用 any() 和 all() 函数
    def check_conditions(conditions):
        print(f"\n8. 检查条件列表 {conditions}:")
        if all(conditions):
            print("  所有条件都为真")
        elif any(conditions):
            print("  至少一个条件为真")
        else:
            print("  所有条件都为假")

    check_conditions([True, True, True])
    check_conditions([True, False, True])
    check_conditions([False, False, False])

    # 9. 条件表达式在列表推导中的应用
    numbers = list(range(-5, 6))
    positive_numbers = [n for n in numbers if n > 0]
    print(f"\n9. 从 {numbers} 中筛选正数:")
    print(f"   结果: {positive_numbers}")

    # 10. 使用 isinstance() 进行类型检查
    def describe_type(obj):
        print(f"\n10. 描述对象 {obj} 的类型:")
        if isinstance(obj, int):    #isinstance()函数可以判断一个对象是否是一个已知的类型，返回True或False
            print("  这是一个整数")
        elif isinstance(obj, float):
            print("  这是一个浮点数")
        elif isinstance(obj, str):
            print("  这是一个字符串")
        elif isinstance(obj, list):
            print("  这是一个列表")
        else:
            print("  这是其他类型")

    describe_type(10)
    describe_type(3.14)
    describe_type("Hello")
    describe_type([1, 2, 3])


def demonstrate_match_case():
    print("Python match...case 示例\n")

    # 1. 基本匹配
    def basic_match(value):
        print(f"1. 基本匹配 ({value}):")
        match value:
            case 0:
                print("  值是零")
            case 1:
                print("  值是一")
            case 2:
                print("  值是二")
            case _:         #_表示匹配任意值
                print("  其他值")

    basic_match(1)
    basic_match(3)

    # 2. 匹配多个值
    def match_multiple(value):
        print(f"\n2. 匹配多个值 ({value}):")
        match value:
            case 0 | 1 | 2:
                print("  值是 0, 1 或 2")
            case _:
                print("  其他值")

    match_multiple(1)
    match_multiple(5)

    # 3. 匹配范围
    def match_range(value):
        print(f"\n3. 匹配范围 ({value}):")
        match value:
            case x if 0 <= x < 10:  #三元运算符的形式，x是变量名，0 <= x < 10是条件
                print("  个位数")
            case x if 10 <= x < 100:
                print("  两位数")
            case _:
                print("  三位数或更大")

    match_range(5)
    match_range(50)
    match_range(500)

    # 4. 结构匹配
    def match_structure(data):
        print(f"\n4. 结构匹配 ({data}):")
        match data:
            case (x, y):
                print(f"  二元组: x={x}, y={y}")
            case [x, y, z]:
                print(f"  三元素列表: x={x}, y={y}, z={z}")
            case {"name": name, "age": age}:
                print(f"  字典: name={name}, age={age}")
            case _:
                print("  不匹配任何已知结构")

    match_structure((1, 2))
    match_structure([1, 2, 3])
    match_structure({"name": "Alice", "age": 30})
    match_structure(42)

    # 5. 类匹配
    class Point:
        def __init__(self, x, y):
            #__init__是构造函数，self是实例对象的引用，x和y是实例对象的属性
            self.x = x
            self.y = y

    def match_class(obj):
        print(f"\n5. 类匹配 ({obj}):")
        match obj:
            case Point(x=0, y=0):
                print("  原点")
            case Point(x=0, y=y):
                print(f"  Y轴上的点 (y={y})")
            case Point(x=x, y=0):
                print(f"  X轴上的点 (x={x})")
            case Point(x=x, y=y):
                print(f"  普通点 (x={x}, y={y})")
            case _:
                print("  不是 Point 对象")

    match_class(Point(0, 0))
    match_class(Point(0, 5))
    match_class(Point(3, 4))
    match_class("Not a point")

    # 6. 带条件的匹配
    def match_with_condition(value):
        print(f"\n6. 带条件的匹配 ({value}):")
        match value:
            case x if x < 0:
                print("  负数")
            case x if x % 2 == 0:
                print("  正偶数")
            case x if x % 2 != 0:
                print("  正奇数")

    match_with_condition(-5)
    match_with_condition(4)
    match_with_condition(7)

    # 7. 使用通配符
    def match_with_wildcard(value):
        print(f"\n7. 使用通配符 ({value}):")
        match value:
            case [1, 2, *rest]:
                print(f"  列表以 1, 2 开头，剩余部分是: {rest}")
            case (1, *middle, 5):
                print(f"  元组以 1 开头，5 结尾，中间部分是: {middle}")
            case _:
                print("  不匹配任何模式")

    match_with_wildcard([1, 2, 3, 4, 5])
    match_with_wildcard((1, 2, 3, 4, 5))
    match_with_wildcard([3, 4, 5])

    # 8. 命名子模式
    def match_named_subpattern(data):
        print(f"\n8. 命名子模式 ({data}):")
        match data:
            case {"point": Point(x=x, y=y) as p}:     #as p是命名子模式，p是变量名，Point(x=x, y=y)是模式，p是变量名，x和y是变量名
                print(f"  包含点的字典: {p}, x={x}, y={y}")
            case _:
                print("  不匹配")

    match_named_subpattern({"point": Point(3, 4)})  #输入的是字典，字典的键是point，值是Point(3, 4)，Point(3, 4)是Point类的实例对象，x=3，y=4
    match_named_subpattern({"not_a_point": (1, 2)})


if __name__ == "__main__":
    demonstrate_conditional_control()
    print("------------------------------------")
    demonstrate_match_case()