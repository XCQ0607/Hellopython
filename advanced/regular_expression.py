#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def regex_pattern_demo():
    """
    演示各种正则表达式模式的用法
    """
    print("1. 基本模式匹配示例")
    text = "Python3 正则表达式教程 2024"

    # 1. 使用 re.match() - 从字符串开头匹配
    pattern = r"Python"
    match_result = re.match(pattern, text)
    print(f"match 'Python':", "匹配成功" if match_result else "匹配失败")

    # 2. 使用 re.search() - 搜索整个字符串
    pattern = r"正则"
    search_result = re.search(pattern, text)
    print(f"search '正则':", "匹配成功" if search_result else "匹配失败")

    # 3. 字符类和特殊字符
    print("\n2. 字符类和特殊字符示例")
    test_str = "abc123DEF!@# \t\n"

    patterns = {
        r"\d+": "匹配数字",
        r"\D+": "匹配非数字",
        r"\w+": "匹配字母数字下划线",
        r"\W+": "匹配特殊字符",
        r"\s+": "匹配空白字符",
        r"\S+": "匹配非空白字符"
    }

    for pattern, desc in patterns.items():
        matches = re.findall(pattern, test_str)
        print(f"{desc} ({pattern}): {matches}")


def regex_groups_demo():
    """
    演示正则表达式分组功能
    """
    print("\n3. 分组匹配示例")

    # 1. 基本分组
    text = "电话号码: 021-12345678"
    pattern = r"(\d{3})-(\d{8})"
    match = re.search(pattern, text)
    if match:
        print(f"区号: {match.group(1)}")
        print(f"电话号码: {match.group(2)}")
        print(f"完整匹配: {match.group(0)}")

    # 2. 命名分组
    text = "生日: 1990年12月25日"
    pattern = r"(?P<year>\d{4})年(?P<month>\d{2})月(?P<day>\d{2})日"
    match = re.search(pattern, text)
    if match:
        print(f"年: {match.group('year')}")
        print(f"月: {match.group('month')}")
        print(f"日: {match.group('day')}")


def regex_modifiers_demo():
    """
    演示正则表达式修饰符的用法
    """
    print("\n4. 修饰符示例")

    # 1. re.IGNORECASE (re.I) - 忽略大小写
    text = "Python python PYTHON"
    matches = re.findall(r'python', text, re.IGNORECASE)
    print(f"忽略大小写匹配: {matches}")

    # 2. re.MULTILINE (re.M) - 多行模式
    text = """第一行
    第二行
    第三行"""
    matches = re.findall(r'^\w+', text, re.MULTILINE)
    print(f"多行模式匹配行首: {matches}")

    # 3. re.DOTALL (re.S) - 点号匹配所有字符
    text = "开始\n结束"
    match_default = re.search(r'开始.结束', text)
    match_dotall = re.search(r'开始.结束', text, re.DOTALL)
    print(f"默认点号匹配: {'成功' if match_default else '失败'}")
    print(f"DOTALL模式: {'成功' if match_dotall else '失败'}")


def regex_methods_demo():
    """
    演示各种正则表达式方法的用法
    """
    print("\n5. 常用方法示例")

    # 1. re.sub() - 替换
    text = "我的电话是 123-4567-8900 和 987-6543-2100"
    new_text = re.sub(r'\d{3}-\d{4}-\d{4}', '***-****-****', text)
    print(f"替换后的文本: {new_text}")

    # 2. re.split() - 分割
    text = "python;java,php:javascript"
    parts = re.split(r'[;,:]', text)
    print(f"分割结果: {parts}")

    # 3. re.finditer() - 迭代匹配
    text = "IP地址: 192.168.1.1 和 10.0.0.1"
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    for match in re.finditer(pattern, text):
        print(f"找到IP: {match.group()} 在位置 {match.span()}")


def regex_compile_demo():
    """
    演示编译正则表达式的用法
    """
    print("\n6. 编译正则表达式示例")

    # 编译正则表达式以提高性能
    pattern = re.compile(r'\b\w+@\w+\.\w+\b')
    test_texts = [
        "联系方式: user@example.com",
        "邮箱是 invalid@email",
        "another.email@domain.com"
    ]

    for text in test_texts:
        match = pattern.search(text)
        if match:
            print(f"找到有效邮箱: {match.group()}")


def main():
    """
    主函数，运行所有示例
    """
    print("=== Python正则表达式综合示例 ===")

    # 运行所有示例
    regex_pattern_demo()
    regex_groups_demo()
    regex_modifiers_demo()
    regex_methods_demo()
    regex_compile_demo()


if __name__ == "__main__":
    main()