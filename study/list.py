list01= ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 读取第二位
print ("list01[1]: ", list01[1])
# 从第二位开始截取到倒数第二位（负数不包含）
print ("list01[1:-2]: ", list01[1:-2])
# 从第二位开始截取到第三位（正数包含）
print("list01[1:3]:", list01[1:3])

#append函数
list01.append('Baidu')
print("list01.append('Baidu'):", list01)

#del函数
del list01[2]
print("del list01[2]:", list01)


#--------------------------------------------------
import operator

def print_separator(title):
    print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")   #\n表示换行，\t表示制表符，*表示重复字符

# 创建初始列表
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry',"z"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print_separator("初始列表")
print(f"fruits: {fruits}")
print(f"numbers: {numbers}")

# 1. len() - 列表元素个数
print_separator("len() - 列表元素个数")
print(f"len(fruits): {len(fruits)}")
print(f"len(numbers): {len(numbers)}")

# 2. max() - 返回列表元素最大值
print_separator("max() - 返回列表元素最大值")
print(f"max(fruits): {max(fruits)}")  # 字母顺序最大,即最后一个字母最大
print(f"max(numbers): {max(numbers)}")

# 3. min() - 返回列表元素最小值
print_separator("min() - 返回列表元素最小值")
print(f"min(fruits): {min(fruits)}")  # 字母顺序最小,即第一个字母最小
print(f"min(numbers): {min(numbers)}")

# 4. list() - 将元组转换为列表
print_separator("list01() - 将元组转换为列表")
tuple_example = ('fig', 'grape', 'honeydew')    # 元组
list_from_tuple = list(tuple_example)
print(f"Original tuple: {tuple_example}")
print(f"List from tuple: {list_from_tuple}")

# 5. append() - 在列表末尾添加新的对象
print_separator("append() - 在列表末尾添加新的对象")
fruits.append('fig')
print(f"fruits after append('fig'): {fruits}")

# 6. count() - 统计某个元素在列表中出现的次数
print_separator("count() - 统计某个元素在列表中出现的次数")
print(f"numbers.count(5): {numbers.count(5)}")

# 7. extend() - 在列表末尾一次性追加另一个序列中的多个值
print_separator("extend() - 在列表末尾一次性追加另一个序列中的多个值")
fruits.extend(['grape', 'honeydew'])
print(f"fruits after extend(['grape', 'honeydew']): {fruits}")  #不存在join函数

# 8. index() - 从列表中找出某个值第一个匹配项的索引位置
print_separator("index() - 从列表中找出某个值第一个匹配项的索引位置")
print(f"fruits.index('banana'): {fruits.index('banana')}")  #不存在find函数

# 9. insert() - 将对象插入列表
print_separator("insert() - 将对象插入列表")
fruits.insert(2, 'kiwi')      # 在索引2处插入'kiwi'
print(f"fruits after insert(2, 'kiwi'): {fruits}")

# 10. pop() - 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print_separator("pop() - 移除列表中的一个元素")
print(f"Popped fruit: {fruits.pop()}")
popped_fruit = fruits.pop()
print(f"Popped fruit: {popped_fruit}")
print(f"fruits after pop(): {fruits}")
print(f"numbers: {numbers}")
popped_number = numbers.pop(3)  # 移除索引为3的元素
print(f"Popped number at index 3: {popped_number}") # 移除索引为3的元素
print(f"numbers after pop(3): {numbers}")

# 11. remove() - 移除列表中某个值的第一个匹配项
print_separator("remove() - 移除列表中某个值的第一个匹配项")
fruits.remove('banana')
print(f"fruits after remove('banana'): {fruits}")

# 12. reverse() - 反向列表中元素
print_separator("reverse() - 反向列表中元素")
fruits.reverse()
print(f"fruits after reverse(): {fruits}")

# 13. sort() - 对原列表进行排序
print_separator("sort() - 对原列表进行排序")
fruits.sort()
print(f"fruits after sort(): {fruits}")
numbers.sort(reverse=True)  # 降序排序
print(f"numbers after sort(reverse=True): {numbers}")

# 14. clear() - 清空列表
print_separator("clear() - 清空列表")
numbers.clear()
print(f"numbers after clear(): {numbers}")

# 15. copy() - 复制列表
print_separator("copy() - 复制列表")
fruits_copy = fruits.copy()
print(f"Original fruits: {fruits}")
print(f"Copied fruits: {fruits_copy}")

# 列表操作符示例
print_separator("列表操作符示例")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"list1: {list1}    list2: {list2}")
print(f"list1 + list2: {list1 + list2}")
print(f"list1 * 3: {list1 * 3}")
print(f"2 in list1: {2 in list1}")

# 列表比较
print_separator("列表比较")
a = [1, 2]
b = [2, 3]
c = [2, 3]
print(f"a: {a}    b: {b}    c: {c}")
print(f"operator.eq(a, b): {operator.eq(a, b)}")
print(f"operator.eq(b, c): {operator.eq(b, c)}")

# 列表推导式示例
print_separator("列表推导式示例")
squares = [x**2 for x in range(10)]
print(f"Squares of numbers 0-9: {squares}")

# 嵌套列表示例
print_separator("嵌套列表示例")
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
print(f"Nested list01: {nested_list}")
print(f"nested_list[0][1]: {nested_list[0][1]}")
print(f"nested_list[1][2]: {nested_list[1][2]}")


