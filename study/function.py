

def print_range(r):
    print(f"Range: {r}")
    print(f"List of range: {list(r)}")
    print(f"Type: {type(r)}")
    print(f"Length: {len(r)}")
    print("First 5 elements (if available):")
    for i, num in enumerate(r): # 枚举迭代器，同时获取索引和值.enumerate()函数可以同时获取索引和值
        #类似in + dict，同时获取dict的键和值，参加dict.py的第65行代码
        if i >= 5:
            break
        print(num, end=" ")
    print("\n")
# -------------------
print("range 函数的用法")
# 1. 基本用法：只有 stop 参数
print("1. 基本用法：只有 stop 参数")
r1 = range(5)   #包括0，不包括5
print_range(r1)

# 2. 指定 start 和 stop
print("2. 指定 start 和 stop")
r2 = range(2, 8)    #包括2，不包括8
print_range(r2)

# 3. 指定 start, stop 和 step
print("3. 指定 start, stop 和 step")
r3 = range(1, 10, 2)
print_range(r3)

# 4. 负步长
print("4. 负步长")
r4 = range(10, 0, -1)    #包括10，不包括0
print_range(r4)

# 5. 空范围
print("5. 空范围")
r5 = range(0)     #空范围
print_range(r5)

# 6. 大范围
print("6. 大范围")
r6 = range(0, 1000000, 100000)
print_range(r6)

# 7. 使用 range 进行迭代
print("7. 使用 range 进行迭代")
for i in range(3):
    print(f"Iteration {i}")

# 8. 使用 range 创建列表
print("\n8. 使用 range 创建列表")
list_from_range = list(range(1, 6))
print(f"List created from range: {list_from_range}")

# 9. 检查成员关系
print("\n9. 检查成员关系")
r7 = range(0, 10, 2)
print(f"Is 4 in {r7}? {4 in r7}")
print(f"Is 5 in {r7}? {5 in r7}")

# 10. 索引和切片
print("\n10. 索引和切片")
r8 = range(0, 10)
print(f"Third element of {r8}: {r8[2]}")
print(f"Slice of {r8}: {r8[2:6]}")    #切片的结果是一个range对象，不是列表，因为range对象是不可变的，不能像列表一样进行切片。即输出range[2:6]

# 11. 比较 range 对象
print("\n11. 比较 range 对象")
r9 = range(0, 5)
r10 = range(0, 5)
r11 = range(0, 6)
print(f"{r9} == {r10}: {r9 == r10}")
print(f"{r9} == {r11}: {r9 == r11}")

# 12. range 的属性
print("\n12. range 的属性")
r12 = range(1, 10, 2)
print(f"Range: {r12}")
print(f"Start: {r12.start}")
print(f"Stop: {r12.stop}")
print(f"Step: {r12.step}")

# ---------------------