# Python数据结构综合示例
from collections import deque  # 导入deque模块，它是一个双端队列，支持从两端添加和删除元素


class DataStructuresDemo:
    def __init__(self):
        self.reset_data()

    def reset_data(self):
        """重置所有数据结构到初始状态"""
        # 列表示例数据
        self.numbers = [1, 2, 3, 4, 5]
        self.fruits = ['apple', 'banana', 'orange']

        # 元组示例数据
        self.point = (10, 20)
        self.person = ('John', 25, 'New York')

        # 集合示例数据
        self.set1 = {1, 2, 3, 4, 5}
        self.set2 = {4, 5, 6, 7, 8}

        # 字典示例数据
        self.student = {
            'name': 'Alice',
            'age': 20,
            'courses': ['Math', 'Physics']
        }

    def demonstrate_lists(self):
        """演示列表的各种操作"""
        print("\n=== 列表操作演示 ===")

        # 基本操作
        print("\n1. 基本列表操作:")
        print(f"原始列表: {self.numbers}")

        # append
        self.numbers.append(6)
        print(f"append(6)后: {self.numbers}")

        # extend
        self.numbers.extend([7, 8])
        print(f"extend([7, 8])后: {self.numbers}")

        # insert
        self.numbers.insert(0, 0)
        print(f"insert(0, 0)后: {self.numbers}")

        # remove
        self.numbers.remove(4)
        print(f"remove(4)后: {self.numbers}")

        # pop
        popped = self.numbers.pop()  # pop()方法返回被弹出的元素（最后一个元素）
        print(f"pop()返回值: {popped}")
        print(f"pop()后: {self.numbers}")

        # 列表推导式
        print("\n2. 列表推导式:")
        squares = [x ** 2 for x in range(1, 6)]
        print(f"1-5的平方: {squares}")

        # 列表作为栈使用
        print("\n3. 列表作为栈使用:")
        stack = []
        for i in range(3):
            stack.append(i)
            print(f"压入 {i}: {stack}")
        while stack:
            print(f"弹出: {stack.pop()}, 剩余: {stack}")

        # 列表作为队列使用
        print("\n4. 使用deque作为队列:")
        queue = deque(
            [1, 2, 3])  # deque是一个双端队列，支持从两端添加和删除元素，比如使用.append()方法添加元素，使用.popleft()方法删除左端元素,.pop方法返回队列最右边的元素并将其从队列中删除
        print(f"初始队列: {queue}")
        queue.append(4)
        print(f"入队4后: {queue}")
        print(f"出队: {queue.popleft()}")  # .popleft()方法返回队列最左边的元素，并将其从队列中删除
        print(f"当前队列: {queue}")

    def demonstrate_tuples(self):  # 虽然demonstrate_tuples函数好像有self参数，但是传入时可为空。在Python中，self是一个约定俗成的参数名，它通常用于表示实例对象本身。
        """演示元组的各种操作"""

        print("\n=== 元组操作演示 ===")

        # 基本操作
        print("\n1. 基本元组操作:")
        print(f"点坐标: {self.point}")
        x, y = self.point  # 解包
        print(f"解包后 - x: {x}, y: {y}")

        # 嵌套元组
        nested = (self.point, (30, 40))
        print(f"嵌套元组: {nested}")

        # 元组方法
        person_tuple = ('Alice', 'Alice', 'Bob', 'Charlie')
        print(f"计数 'Alice': {person_tuple.count('Alice')}")
        print(f"'Bob'的索引: {person_tuple.index('Bob')}")


    def demonstrate_sets(self):
        """演示集合的各种操作"""
        print("\n=== 集合操作演示 ===")

        print(f"集合1: {self.set1}")
        print(f"集合2: {self.set2}")

        # 集合运算
        print(f"\n交集: {self.set1 & self.set2}")
        print(f"并集: {self.set1 | self.set2}")
        print(f"差集(set1 - set2): {self.set1 - self.set2}")
        print(f"对称差集: {self.set1 ^ self.set2}")

        # 集合推导式
        squares_set = {x ** 2 for x in range(1, 6)}
        print(f"\n集合推导式(1-5的平方): {squares_set}")

        # 集合方法
        test_set = {1, 2, 3}
        test_set.add(4)
        print(f"\n添加元素后: {test_set}")
        test_set.remove(2)
        print(f"删除元素后: {test_set}")

        # 子集和超集
        set_a = {1, 2}
        set_b = {1, 2, 3, 4}
        print(f"\n{set_a} 是 {set_b} 的子集: {set_a.issubset(set_b)}")
        print(f"{set_b} 是 {set_a} 的超集: {set_b.issuperset(set_a)}")


    def demonstrate_dictionaries(self):
        """演示字典的各种操作"""
        print("\n=== 字典操作演示 ===")

        # 基本操作
        print("\n1. 基本字典操作:")
        print(f"原始字典: {self.student}")

        # 添加/修改元素
        self.student['grade'] = 'A'
        print(f"添加grade后: {self.student}")

        # 获取方法
        print(f"\n2. 字典获取方法:")
        print(f"使用get()获取age: {self.student.get('age')}")
        print(f"使用get()获取不存在的键(带默认值): {self.student.get('phone', 'Not found')}")
        print(f"使用get()获取不存在的键(不带默认值): {self.student.get('phone')}")
        print(f"使用in运算符检查键是否存在: {'name' in self.student}")
        print(f"使用in运算符检查不存在的键: {'phone' in self.student}")
        print(f"使用pop()删除元素: {self.student.pop('name')}")
        print(f"删除元素后: {self.student}")
        try:
            del self.student['age']
            print(f"使用del删除元素: {self.student}")
            print(f"使用del删除不存在的键会抛出异常: {self.student.pop('age')}")
        except KeyError:
            print("KeyError: 'age' not found")


        # 字典推导式
        squares_dict = {x: x ** 2 for x in range(1, 6)}
        print(f"\n3. 字典推导式(1-5的平方): {squares_dict}")

        # 字典视图
        print("\n4. 字典视图:")
        print(f"键视图keys: {list(self.student.keys())}")
        print(f"值视图: {list(self.student.values())}")
        print(f"键值对视图: {list(self.student.items())}")

        # 字典合并
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        merged = {**dict1, **dict2}  # Python 3.5+，使用**运算符合并字典
        print(f"\n5. 合并字典: {merged}")


    def demonstrate_advanced_operations(self):
        """演示高级操作和技巧"""
        print("\n=== 高级操作演示 ===")

        # enumerate使用   这个函数可以同时获取元素的索引和值
        print("\n1. enumerate使用:")
        for i, fruit in enumerate(self.fruits, 1):  # 从1开始计数，默认是0(index)
            print(f"水果 {i}: {fruit}")

        # zip使用
        print("\n2. zip使用:")
        numbers = [1, 2, 3]
        letters = ['a', 'b', 'c']
        for num, letter in zip(numbers, letters):
            print(f"数字: {num}, 字母: {letter}")

        # 推导式中的条件
        print("\n3. 带条件的推导式:")
        even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
        print(f"偶数的平方: {even_squares}")

        # 嵌套数据结构
        print("\n4. 嵌套数据结构:")
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # 转置矩阵
        transposed = [[row[i] for row in matrix] for i in range(3)]
        untransposed = list(map(lambda x: list(x), zip(*transposed)))   # 使用map函数和lambda表达式实现转置,map函数作用是将一个函数应用到一个列表的每个元素上，返回一个新的列表。
        print(f"原始矩阵: {matrix}")
        print(f"转置后: {transposed}")
        print(f"untransposed: {untransposed}")


def main():
    demo = DataStructuresDemo()

    # 演示所有数据结构操作
    demo.demonstrate_lists()
    demo.demonstrate_tuples()
    demo.demonstrate_sets()
    demo.demonstrate_dictionaries()
    demo.demonstrate_advanced_operations()


if __name__ == "__main__":
    main()
