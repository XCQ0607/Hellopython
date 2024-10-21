class CustomList:
    def __init__(self, *args):  #self是实例化对象
        # 初始化方法，可以接受任意数量的参数
        self.items = list(args) # 初始化实例属性

    def __str__(self):
        # 返回对象的字符串表示
        return f"CustomList({', '.join(map(str, self.items))})"

    def __repr__(self):
        # 返回对象的"官方"字符串表示
        return self.__str__()

    def __len__(self):
        # 返回对象的长度
        return len(self.items)

    def __getitem__(self, index):
        # 允许使用索引访问实例化对象的元素
        return self.items[index]

    def __setitem__(self, index, value):
        # 允许使用索引设置元素值
        self.items[index] = value

    def __iter__(self):
        # 使对象可迭代
        return iter(self.items)

    def __contains__(self, item):
        # 实现 'in' 操作符
        return item in self.items

    def __add__(self, other):
        # 实现加法操作
        if isinstance(other, CustomList):
            return CustomList(*(self.items + other.items))
        elif isinstance(other, list):
            return CustomList(*(self.items + other))
        else:
            raise TypeError("Unsupported operand type for +")

    def __eq__(self, other):
        # 实现相等性比较
        if isinstance(other, CustomList):   # 判断other是否是CustomList类型
            return self.items == other.items
        return False

    def __lt__(self, other):    #ls全称是less than
        # 实现小于比较
        if isinstance(other, CustomList):
            return len(self) < len(other)
        return NotImplemented

    def __call__(self, index):
        # 使对象可调用
        return self.items[index]

# 使用示例
if __name__ == "__main__":
    # 创建CustomList对象
    cl1 = CustomList(1, 2, 3, 4, 5) # 创建CustomList对象-cl1
    cl2 = CustomList(6, 7, 8)       # 创建CustomList对象-cl2

    print("1. __str__ and __repr__:")
    print(cl1)  # 使用__str__,这里的print函数被重写了
    print(repr(cl1))  # 使用__repr__

    print("\n2. __len__:")
    print(f"Length of cl1: {len(cl1)}")

    print("\n3. __getitem__ and __setitem__:")
    print(f"Third item of cl1: {cl1[2]}")
    cl1[2] = 10
    print(f"cl1 after changing third item: {cl1}")

    print("\n4. __iter__:")
    print("Iterating over cl1:")    # 迭代CustomList对象的元素
    for item in cl1:
        print(item, end=" ")
    print()

    print("\n5. __contains__:")
    print(f"Is 4 in cl1? {4 in cl1}")
    print(f"Is 10 in cl1? {10 in cl1}")

    print("\n6. __add__:")
    cl3 = cl1 + cl2
    print(f"cl1 + cl2 = {cl3}")

    print("\n7. __eq__:")
    cl4 = CustomList(1, 2, 10, 4, 5)    # 创建CustomList对象-cl4
    print(f"cl1 == cl4? {cl1 == cl4}")

    print("\n8. __lt__:")
    print(f"cl1 < cl2? {cl1 < cl2}")
    #虽然说是less than，但是>也是可以的

    print("\n9. __call__:")
    print(f"cl1(3) = {cl1(3)}") #cl1()是调用__call__方法，传入的参数是3
# 这个代码示例展示了以下魔法方法：
#
# __init__(self, *args): 初始化方法，可以接受任意数量的参数。
# __str__(self): 返回对象的字符串表示，用于 print() 和 str()。
# __repr__(self): 返回对象的"官方"字符串表示，用于 repr()。
# __len__(self): 返回对象的长度，用于 len() 函数。
# __getitem__(self, index): 允许使用索引访问元素，如 obj[index]。
# __setitem__(self, index, value): 允许使用索引设置元素值，如 obj[index] = value。
# __iter__(self): 使对象可迭代，用于 for 循环。
# __contains__(self, item): 实现 in 操作符。
# __add__(self, other): 实现加法操作，如 obj1 + obj2。
# __eq__(self, other): 实现相等性比较，如 obj1 == obj2。
# __lt__(self, other): 实现小于比较，如 obj1 < obj2。
# __call__(self, index): 使对象可调用，如 obj(index)。
# 注意事项：
#
# 这些方法的命名都是以双下划线开始和结束的。
# 有些方法（如 __add__）应该返回一个新对象，而不是修改现有对象。
# 对于比较操作（如 __eq__ 和 __lt__），应该考虑类型检查，并在不适用时返回 NotImplemented。
# __repr__ 应该返回一个有效的Python表达式字符串，如果可能的话。
# 相关函数：
#
# __str__ 和 __repr__ 的区别：__str__ 用于为终端用户提供更友好的输出，而 __repr__ 应该提供更详细、精确的输出，主要用于调试。
# 除了 __lt__，还有 __le__（小于等于）、__gt__（大于）和 __ge__（大于等于）用于比较操作。
# __add__ 的反向操作是 __radd__，用于处理 other + self 的情况。