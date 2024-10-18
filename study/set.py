def print_separator(message):
    print("\n" + "=" * 50)
    print(message)
    print("=" * 50)
#set集合的详细性质：
# 1. 无序性：集合中的元素没有固定的顺序，每次打印的顺序可能不同。
# 2. 唯一性：集合中的元素是唯一的，不允许重复。
# 3. 可变性：可以添加、删除和修改元素。
# 4. 不可变性：集合中的元素必须是不可变的，例如数字、字符串或元组。
# 5. 可迭代性：可以使用for循环遍历其中的元素。
# 6. 可哈希性：集合中的元素必须是可哈希的，即它们必须是不可变的（例如数字、字符串、元组），并且必须具有唯一的哈希值。

# 可哈希性（Hashability）是 Python 中的一个重要概念，尤其是在讨论集合（set）和字典（dict）等数据结构时。
# 可哈希性的定义：
# 一个对象是可哈希的，如果它有一个在其生命周期内永不改变的哈希值（hash value）。
# 可哈希对象必须实现 hash() 方法和 eq() 方法。
# 可哈希性的特点：
# 不可变性：通常，可哈希对象都是不可变的。这是因为如果对象可以改变，它的哈希值也可能改变，这会导致在基于哈希的集合中出现问题。
# 唯一性：相等的对象必须具有相同的哈希值。
# Python 中的可哈希对象：
# 所有的不可变内置类型都是可哈希的，如：int, float, str, tuple, frozenset。
# 自定义类的实例默认是可哈希的（基于其 id）。
# 为什么需要可哈希性：
# 集合（set）和字典（dict）的键需要可哈希对象。这是因为这些数据结构内部使用哈希表来实现快速查找。
# 可哈希性允许对象被用作字典的键或集合的元素。

# 集合本身是可变的：我们可以添加和删除元素。
# 集合中的元素必须是不可变的：我们可以添加数字、字符串和元组，但不能添加列表。
print_separator("验证集合的可变性与不可变性")
# 创建一个空集合
my_set = set()
# 添加元素（展示集合的可变性）
my_set.add(1)
my_set.add("hello")
my_set.add((1, 2, 3))  # 元组是不可变的，所以可以添加
print("集合内容:", my_set)
# 尝试添加可变对象（会引发错误）
try:
    my_set.add([4, 5, 6])  # 列表是可变的，不能添加到集合中
except TypeError as e:
    print("错误:my_set.add([4, 5, 6])", e)
# 移除元素（再次展示集合的可变性）
my_set.remove("hello")


# ----------------------


# 创建集合
print_separator("创建集合")

# 使用花括号创建集合     不同于字典花括号的是，花括号里面的元素是键值对(:)，而不是键
fruits = {"apple", "banana", "cherry"}
print("使用花括号创建的集合:", fruits)

# 使用set()函数创建集合
numbers = set([1, 2, 3, 4, 5, 5])      # 注意这里的[]是列表的意思，而不是集合的意思，列表是有序的，集合是无序的，列表可以有重复的元素，集合不能有重复的元素，列表可以通过索引访问元素，集合不能通过索引访问元素，列表可以通过切片访问元素，集合不能通过切片访问元素，列表可以通过for循环访问元素，集合不能通过for循环访问元素，列表可以通过列表推导式
print("使用set()函数创建的集合:", numbers)

# 从字符串创建集合
char_set = set("hello")
print("从字符串创建的集合:", char_set)

# 集合的基本操作
print_separator("集合的基本操作")

# 添加元素
fruits.add("orange")
print("添加元素后的fruits集合:", fruits)

# 移除元素
fruits.remove("banana")  # 如果元素不存在会引发KeyError
print("移除元素后的fruits集合:", fruits)

# 尝试移除不存在的元素
try:
    fruits.remove("grape")
except KeyError:
    print("尝试移除不存在的元素'grape'引发KeyError")

# 安全地移除元素
fruits.discard("cherry")  # 如果元素不存在不会引发错误
print("安全移除元素后的fruits集合:", fruits)

# 随机移除并返回一个元素
popped = fruits.pop()   #不同于列表的pop()方法，列表的pop()方法是移除列表中的最后一个元素，而集合的pop()方法是随机移除一个元素。
print(f"随机移除的元素: {popped}")
print("pop操作后的fruits集合:", fruits)

# 清空集合
fruits.clear()
print("清空后的fruits集合:", fruits)

# 集合操作
print_separator("集合操作")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
a = set('abracadabra')
b = set('alacazam')
#a,b类型都是set

# 并集
union_set = set1.union(set2)
print("set1和set2的并集:", union_set)
print("set1和set2的并集 (使用|)",set1|set2)


# 交集
intersection_set = set1.intersection(set2)
print("set1和set2的交集:", intersection_set)
print("set1和set2的交集 (使用&)",set1&set2)

# 差集
difference_set = set1.difference(set2)
print("set1和set2的差集 (在set1中但不在set2中的元素):", difference_set)
print("set1和set2的差集 (使用-)",set1-set2)

# 对称差集
symmetric_difference_set = set1.symmetric_difference(set2)
print("set1和set2的对称差集 (在set1或set2中，但不同时在两个集合中的元素):", symmetric_difference_set)
print("set1和set2的对称差集 (使用^)",set1^set2)

# 子集和超集
subset = {1, 2, 3}
print(f"{subset} 是 {set1} 的子集:", subset.issubset(set1))
print(f"{set1} 是 {subset} 的超集:", set1.issuperset(subset))

# 集合的其他方法
print_separator("集合的其他方法")

# 复制集合
set3 = set1.copy()
print("复制set1得到的新集合:", set3)

# 判断两个集合是否有相同元素
print("set1和set2是否有相同元素:", set1.isdisjoint(set2))

# 更新集合
set1.update(set2)
print("用set2更新set1后的结果:", set1)

# 集合推导式
print_separator("集合推导式")

# 创建一个包含1到10的平方数的集合
squares = {x**2 for x in range(1, 11)}
print("1到10的平方数集合:", squares)

# 创建一个包含1到20中能被3整除的数的集合
divisible_by_3 = {x for x in range(1, 21) if x % 3 == 0}
print("1到20中能被3整除的数的集合:", divisible_by_3)

# 集合的性能优势
print_separator("集合的性能优势")

import time

# 创建一个大列表和一个大集合
big_list = list(range(1000000))
big_set = set(range(1000000))

# 测试列表查找性能
start = time.time()
999999 in big_list
end = time.time()
print(f"在列表中查找元素耗时: {end - start:.6f} 秒")

# 测试集合查找性能
start = time.time()
999999 in big_set
end = time.time()
print(f"在集合中查找元素耗时: {end - start:.6f} 秒")

# 集合的实际应用场景
print_separator("集合的实际应用场景")

# 1. 去重
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))
print("去重后的列表:", unique_numbers)

# 2. 查找共同元素
user1_friends = {"Alice", "Bob", "Charlie"}
user2_friends = {"Bob", "David", "Eve"}
common_friends = user1_friends & user2_friends
print("共同好友:", common_friends)

# 3. 数学集合操作
students_math = {"Alice", "Bob", "Charlie"}
students_physics = {"Bob", "David", "Eve"}
all_students = students_math|students_physics
print("学习数学或物理的所有学生:", all_students)

# 4. 快速成员检查
valid_users = {"user1", "user2", "user3"}
user = "user2"
print(f"{user} 是否是有效用户:", user in valid_users)