#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def regex_pattern_demo():
    """
    演示各种正则表达式模式的用法
    """
    print("1. 基本模式匹配示例")
    text = "我的Python3 正则表达式教程 2024"

    # 1. 使用 re.match() - 从字符串开头匹配
    pattern = r"Python"     #raw字符串，用于表示原始字符串，不进行转义处理
    match_result = re.match(pattern, text)  #返回类型为Match对象
    print(match_result)
    print(f"match '{pattern}':", "匹配成功" if match_result else "匹配失败")

    # 2. 使用 re.search() - 搜索整个字符串
    pattern = r"正则"
    search_result = re.search(pattern, text)
    print(f"search '{pattern}':", "匹配成功" if search_result else "匹配失败")

    # 3. 字符类和特殊字符
    print("\n2. 字符类和特殊字符示例")
    test_str = "abc123DEF!@#__ \t\n"

    patterns = {
        r"\d+": "匹配数字",
        r"\D+": "匹配非数字",
        r"\w+": "匹配字母数字下划线",
        r"\W+": "匹配特殊字符",   #有：!,@,#,_,空格、制表符、换行符
        r"\s+": "匹配空白字符",     #空格、制表符、换行符
        r"\S+": "匹配非空白字符"
    }
    #re.findall()返回所有匹配的字符串列表
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
    # r：表示这是一个原始字符串，里面的反斜杠 \ 不会被当作转义字符。这在正则表达式中很有用，因为正则表达式经常用到反斜杠。
    # (\d{3})：这是一个捕获组。\d表示匹配任意数字（0 - 9）。{3}表示前面的 \d必须恰好出现3次。所以，(\d{3})会匹配3个连续的数字，并且把这三个数字捕获为一个组。
    # -：表示匹配短横线字符 - 本身。
    # (\d{8})：这又是一个捕获组。和前面类似，\d{8}表示匹配8个连续的数字，并且把这八个数字捕获为一个组。
    # 综上所述，这个正则表达式
    # r"(\d{3})-(\d{8})"
    # 会匹配形如 “123 - 45678901” 这样的字符串，其中 “123” 是第一个捕获组，“45678901” 是第二个捕获组。
    # pattern = r"(\d{3})-?(\d{8})"
    #? 符号来表示前面的字符是可选的，即可以出现0次或1次。
    pattern1 = r"(\d{3}-?\d{1})(\d{7})"
    #匹配前四个数字和后七个数字，并且 - 符号在第三个数字后面且可有可无

    patterns1 = {
        "pattern0" : r"(\d{3})-(\d{8})",
        "pattern1" : r"(\d{3}-?\d{1})(\d{7})"
    }
    for pat,pattern in patterns1.items():
        match = re.search(pattern, text)
        if match:
            print(pat)
            print(f"找到匹配: {match.group()}")
            print(f"区号: {match.group(1)}")
            print(f"电话号码: {match.group(2)}")
            print(f"完整匹配: {match.group(0)}")
            #group(0)与group()是一样的，都是返回整个匹配的字符串
    print("----------------------")
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
    print("re.IGNORECASE (re.I) - 忽略大小写")
    text = "Python python PYTHON"
    matches = re.findall(r'python', text, re.IGNORECASE)
    print(f"忽略大小写匹配: {matches}")

    # 2. re.MULTILINE (re.M) - 多行模式     即可以匹配多行文本的模式
    print("re.MULTILINE (re.M) - 多行模式")
    text = """第一行
    第二行
    第三行"""
    matches = re.findall(r'^\w+', text ,re.MULTILINE)   #^\w+匹配以字母开头的单词，\w表示字母数字下划线，+表示匹配一个或多个字符，^表示匹配行首
    print(f"多行模式匹配行首: {matches}")

    text = """
    first line
    second line
    third line
    """
    # 不使用 re.MULTILINE
    print("不使用re.MULTILINE")
    matches_without_m = re.findall(r'^', text)
    print(matches_without_m)  # 输出：['']，只匹配到字符串的开始
    # 使用 re.MULTILINE
    print("使用re.MULTILINE")
    matches_with_m = re.findall(r'^', text, re.MULTILINE)
    print(matches_with_m)  # 输出：['', '', '', '']，匹配到每一行的开始（包括整个字符串的开始）

    # re.MULTILINE（或简写为re.M）在正则表达式中是一个重要的标志，它影响 ^ 和$的行为。在默认情况下， ^ 只匹配字符串的开始，$只匹配字符串的结束。但是，当使用了re.MULTILINE标志后， ^ 还会匹配每一行的开始（即换行符\n之后的位置），而$还会匹配每一行的结束（即换行符\n之前的位置）。
    # 使用了re.MULTILINE标志， ^ 和 $ 会匹配每一行的开头和结尾。

    # 3. re.DOTALL (re.S) - 点号匹配所有字符
    print("re.DOTALL (re.S) - 点号匹配所有字符")
    text = "开始\n结束"
    match_default = re.search(r'开始.结束', text)
    match_dotall = re.search(r'开始.结束', text, re.DOTALL)
    print(f"默认点号匹配: {'成功' if match_default else '失败'}")
    print(f"DOTALL模式: {'成功' if match_dotall else '失败'}")

    # 4. re.VERBOSE (re.X) - 详细模式
    print("re.VERBOSE (re.X) - 详细模式")
    text = """
    这是一个
    多行文本
    """
    pattern = r"""
    ^\s*这是一个    #匹配文本“这是一个”
    .*                #匹配除了换行符之外的任意数量的任意字符
    多行文本\s*$          #匹配文本“多行文本”
    """
    match = re.search(pattern, text, re.VERBOSE|re.DOTALL|re.MULTILINE)
    print(f"详细模式匹配: {'成功' if match else '失败'}")
    #\s*表示匹配零个或多个空格，如果不加这个，会导致匹配错误。因为在re.VERBOSE模式下，会忽略这些空白符(换行符，制表符，回车符，空格)
    #或者说在text后加上.strip()，它的作用是删除字符串开头和结尾的空白符（包括换行符，制表符，回车符，空格）。
    # re.VERBOSE（或re.X），它允许你在正则表达式中加入空白符（空格、换行、制表符等）和注释来增强可读性。这些空白符在正则表达式中将被忽略，除非它们位于字符类（[]）中或者前面有反斜杠（\）
    # ^ 表示一行的开始。
    # 这是一个 会匹配文本“这是一个”。
    # .* 默认情况下会匹配除了换行符之外的任意数量的任意字符。在re.DOTALL（或re.S）模式下，它才会匹配包括换行符在内的任意字符。
    # 多行文本$ 会尝试匹配文本“多行文本”位于一行的末尾。

def regex_methods_demo():
    """
    演示各种正则表达式方法的用法
    """
    print("\n5. 常用方法示例")

    # 1. re.sub() - 替换
    print("re.sub() - 替换示例")
    text = "我的电话是 123-4567-8900 和 987-6543-2100"
    new_text = re.sub(r'\d{3}-\d{4}-\d{4}', '***-****-****', text)  #参数:re.sub(要替换的模式，替换后的文本，要处理的文本)
    print(f"替换后的文本: {new_text}")

    # 2. re.split() - 分割
    print("re.split() - 分割示例")
    text = "python;java,php:javascript"
    parts = re.split(r'[;,:]', text)    #参数：re.split(r'[分隔符1，分隔符2，分隔符3，……]', 要处理的文本)
    print(f"分割结果: {parts}")

    # 3. re.finditer() - 迭代匹配
    print("re.finditer() - 迭代匹配示例")
    #其与re.findall()的区别在于，re.finditer()返回一个迭代器，而re.findall()返回一个列表。
    text = "IP地址: 192.168.1.1 和 10.0.0.1"
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    #pattren1 = r'\d{3}\.\d{3}\.\d{3}\.\d{3}'   d{1,3}表示1-3个数字，而ｄ｛３｝表示3个数字
    for match in re.finditer(pattern, text):
        print(f"找到IP: {match.group()} 在位置 {match.span()}")

    pattern_valid_ip = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    text1 = "IP地址（包含有效与无效）: IP_ADDRESS, IP_ADDRESS, 256.0.0.1, 192.168.0.256"
    for match in re.finditer(pattern_valid_ip, text1):
        print(f"找到有效IP: {match.group()} 在位置 {match.span()}")


def regex_compile_demo():
    """
    演示编译正则表达式的用法
    """
    print("\n6. 编译正则表达式示例")

    # 编译正则表达式以提高性能
    pattern = re.compile(r'\b\w+@\w+\.\w+\b,re.I')   #\b表示单词边界，\w表示字母数字下划线，+表示匹配一个或多个字符
    test_texts = [
        "联系方式: user@example.com",
        "邮箱是 invalid@email",
        "another.email@domain.com"
    ]

    for text in test_texts:
        #从re.search(正则表达式，要处理的文本)转变为 封装的正则表达式对象.search(要处理的文本)
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

#正则表达式修饰符
#re.I（re.IGNORECASE）：忽略大小写。
#re.M（re.MULTILINE）：多行模式。
#re.S（re.DOTALL）：点号匹配所有字符，包括换行符。
#re.X（re.VERBOSE）：详细模式，允许在正则表达式中添加注释和空白符。
#re.ASCII：仅匹配ASCII字符。
#re的方法
#re.sub()：替换匹配的字符串。 参数：re.sub(要替换的模式，替换后的文本，要处理的文本)。
#re.split()：分割字符串。  参数：re.split(r'[分隔符1，分隔符2，分隔符3，……]', 要处理的文本)。
#re.finditer()：迭代匹配。    参数：re.finditer(正则表达式，要处理的文本)。
#re.compile()：编译正则表达式，提高性能。   参数：re.compile(正则表达式，flags(修饰符))。
#re.match()：从字符串开头匹配，与search()的区别在于只能在text的最开始     参数：re.match(正则表达式，要处理的文本)。
#re.search()：搜索整个字符串。     参数：re.search(正则表达式，要处理的文本)。
#re.findall()：返回所有匹配的字符串列表。   参数：re.findall(正则表达式，要处理的文本)。
#re.fullmatch()：完全匹配整个字符串。    参数：re.fullmatch(正则表达式，要处理的文本)。