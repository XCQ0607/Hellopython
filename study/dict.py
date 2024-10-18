# 创建一个示例字典
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": {"Math": 90, "Physics": 85, "Programming": 95}
}

def demonstrate_dictionary_operations():
    print("1. 创建和访问字典:")
    print(f"学生信息: {student}")
    print(f"学生姓名: {student['name']}")
    print(f"数学成绩: {student['grades']['Math']}")

    print("\n2. 修改字典:")
    student["age"] = 21  # 直接赋值修改
    student["grades"]["Math"] = 92  # 修改嵌套字典的值
    print(f"更新后的学生信息: {student}")

    print("\n3. 添加新键值对:")
    student["email"] = "alice@example.com"  # 如果键不存在，会添加新的键值对
    student["grades"]["History"] = 88  # 添加新的嵌套字典键值对
    print(f"添加邮箱后的学生信息: {student}")
    #可将元组作为键值：student[("A","B")] = ["1",2]

    print("\n4. 删除键值对:")
    del student["email"]  # 使用del关键字删除键值对
    print(f"删除邮箱后的学生信息: {student}")

    print("\n5. 字典方法:")
    # keys()方法：返回所有键的视图
    print(f"所有键: {student.keys()}")
    # values()方法：返回所有值的视图
    print(f"所有值: {student.values()}")
    # items()方法：返回所有键值对的视图
    print(f"所有键值对: {student.items()}")

    print("\n6. 获取值 (使用get方法):")
    # get(key[, default])：如果键存在返回对应的值，否则返回默认值（如果提供）
    print(f"专业: {student.get('major', 'Not specified')}")
    print(f"地址: {student.get('address', 'Not specified')}")

    print("\n7. 更新字典:")
    # update([other])：使用另一个字典或可迭代的键值对更新当前字典
    new_info = {"address": "123 Main St", "phone": "555-1234"}
    student.update(new_info)    # 合并字典
    print(f"更新后的学生信息: {student}")

    print("\n8. 检查键是否存在:")
    # 使用in运算符检查键是否存在
    print(f"'name' 是否在字典中: {'name' in student}")
    print(f"'email' 是否在字典中: {'email' in student}")

    print("\n9. 字典的pop和popitem方法:")
    # pop(key[, default])：删除指定键并返回其值，如果键不存在则返回默认值
    age = student.pop("age", "Unknown")
    print(f"移除的年龄: {age}")
    # popitem()：删除并返回最后插入的键值对（在3.7+版本中是最后一个，之前版本中是随机的）
    last_item = student.popitem()
    print(f"移除的最后一项: {last_item}")
    print(f"pop和popitem后的学生信息: {student}")

    print("\n10. 字典推导式:")
    # 创建一个新字典，将原字典中的值增加10%
    increased_grades = {subject: score * 1.1 for subject, score in student['grades'].items()}   #这里的subject是键，score是值,subject，score来自原字典，原因是for循环是从原字典中获取键值对，for两个值，则subject对应键，score对应值
    print(f"提高10%后的成绩: {increased_grades}")

    print("\n11. 字典的fromkeys方法:")
    # fromkeys(iterable[, value])：创建一个新字典，以iterable中的元素为键，value为值
    new_student = dict.fromkeys(['name', 'age', 'major'], 'Unknown')
    print(f"使用fromkeys创建的新字典: {new_student}")

    print("\n12. 字典的copy方法:")
    # copy()：返回字典的浅拷贝
    copied_student = student.copy()
    print(f"复制的学生信息: {copied_student}")

    #dict函数
    #dict(iterable, **kwargs)：创建一个新字典，可选的**kwargs参数用于指定键值对
    new_student = dict(name="Bob", age=22, major="Engineering")
    print(f"使用dict函数创建的新字典: {new_student}")

    print("\n13. 清空字典:")
    # clear()：清空字典中的所有项
    student.clear()
    print(f"清空后的学生信息: {student}")

# 运行示例

if __name__ == '__main__':
    demonstrate_dictionary_operations()

#不要以标准库中的文件名命名代码树库中的文件，这样会导致引用错误的模块