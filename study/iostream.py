import os
import pickle
import sys
from datetime import datetime


def demonstrate_output_formatting():
    """展示各种输出格式化方法"""
    print("\n=== 输出格式化示例 ===")

    # 1. str.format() 方法
    print("\n1. str.format() 方法示例:")
    name = "Python"
    version = 3.9
    print("1.1 基本替换: {} 版本 {}".format(name, version))
    print("1.2 索引替换: {1} 版本 {0}".format(version, name))
    print("1.3 命名替换: {lang} 版本 {ver}".format(lang=name, ver=version))

    # 2. 格式化规范
    print("\n2. 数字格式化:")
    pi = 3.14159265359
    print("2.1 浮点数精度: {:.2f}".format(pi))   #:.2f 表示保留两位小数
    print("2.2 百分比: {:.1%}".format(0.8569))   #:.1% 表示保留一位小数(四舍五入)并显示为百分比
    print("2.3 科学计数: {:.2e}".format(1000000))   #:.2e 表示保留两位小数并显示为科学计数法

    # 3. 对齐和填充
    print("\n3. 文本对齐:")
    print("3.1 居中对齐: '{:^20}'".format("center"))
    print("3.2 左对齐: '{:<20}'".format("left"))
    print("3.3 右对齐: '{:>20}'".format("right"))
    print("3.4 填充: '{:*^20}'".format("filled"))


def demonstrate_file_operations():
    """展示文件操作的各种方法"""
    print("\n=== 文件操作示例 ===")

    filename = "test_file.txt"
    print(f"文件名: {filename}")
    filename1 = "test_file1.txt"
    print(f"文件名1（纯英文--后续使用seek）: {filename1}")


    # 1. 写入test_file.txt
    print("\n1. 写入文件test_file.txt示例:")
    with open(filename, 'w', encoding='utf-8') as f:    # 打开文件，并指定编码为'utf-8'，以写入模式打开，as f表示将文件对象赋值给f，with语句会自动关闭文件，无需手动关闭文件
        f.write("第一行：基本写入\n")
        f.writelines(["第二行：writelines方法\n", "第三行：多行写入\n"])
        print("写入完成")
    # 2. 不自动关闭文件
    print("\n1.1 不自动关闭文件示例:")
    f = open(filename, 'a', encoding='utf-8')    # a 表示以追加模式打开，不会覆盖原文件内容，而是在原文件末尾添加内容
    f.write("第四行：不自动关闭文件\n")
    f.close()
    print("写入完成")
    #写入test_file1.txt
    print("\n1.2 写入文件test_file1.txt示例(纯英文):")
    with open(filename1, 'w', encoding='utf-8') as f:
        f.write("First sentence :Hello!\n")
        f.writelines(["Second sentence :Hello!\n", "Third sentence :Hello!\n"])
        print("写入完成")



    # 2. 读取文件
    print("\n2. 读取文件示例:")
    with open(filename, 'r', encoding='utf-8') as f:
        print("2.1 read()方法读取全部:")
        print(f.read())

    with open(filename, 'r', encoding='utf-8') as f:
        print("\n2.2 readline()方法逐行读取:")
        while True:
            line = f.readline()
            if not line:    # 如果读取到的行是空行，说明已经读取到了文件末尾
                break
            print(f"读取行: {line.strip()}")    # strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。

    with open(filename, 'r', encoding='utf-8') as f:
        print("\n2.3 readlines()方法读取所有行:")
        lines = f.readlines()
        print(f"所有行: {lines}")

    # 3. 文件指针操作
    print("\n3. 文件指针操作:")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"3.1 文件总长度: {len(content)} 个字符")
        # 使用字符串切片替代seek操作
        print(f"3.2 读取前10个字符:\n{content[:10]}")    # 使用字符串切片替代seek操作
        print(f"3.3 读取第5个到第15个字符:\n{content[4:14]}")
        #seek操作在这里会报错，如f.seek(5)
        #在 UTF-8 编码中，一个中文字符通常占用 3 个字节，而 seek 操作是按字节移动的，所以当我们移动到第 5 个字节位置时，可能刚好落在了一个中文字符的中间，导致解码失败。
        #想要使用seek输出中文，需要使用二进制模式打开文件，然后使用read()方法读取文件内容，再使用decode()方法将字节转换为字符串。

    #4.seek操作读取
    print("\n4. 读取文件test_file1.txt示例(纯英文):")
    with open(filename1, 'r') as f:
        print("f.seek(2) 再f.read(1) 读取一个字节:")
        f.seek(2) # 移动到文件的第5个字节位置
        content = f.read(1) # 读取一个字节
        print(f"文件第三个字符: \n{content} ")
        #文件所有内容
        f.seek(0) # 移动到文件的开头
        print(f"文件所有内容: {f.read()}")




def demonstrate_pickle_operations():
    """展示pickle序列化操作"""
    print("\n=== Pickle序列化示例 ===")

    # 1. 创建测试数据
    test_data = {
        'string': 'Hello World',
        'number': 42,
        'list': [1, 2, 3],
        'dict': {'a': 1, 'b': 2},
        'date': datetime.now()
    }

    filename = "test_pickle.pkl"

    # 2. 序列化到文件
    print("\n1. 序列化数据:")
    with open(filename, 'wb') as f:
        pickle.dump(test_data, f)
        print("数据已序列化到文件")

    # 3. 从文件反序列化
    print("\n2. 反序列化数据:")
    with open(filename, 'rb') as f:
        loaded_data = pickle.load(f)
        print("反序列化的数据:")
        for key, value in loaded_data.items():
            print(f"{key}: {value}")


def demonstrate_input_operations():
    """展示输入操作"""
    print("\n=== 输入操作示例 ===")

    # 1. 基本输入
    name = input("\n1. 基本输入示例 - 请输入你的名字: ")
    print(f"你好, {name}!")

    # 2. 数值输入与转换
    try:
        age = int(input("2. 数值输入示例 - 请输入你的年龄: "))
        print(f"明年你将会 {age + 1} 岁")
    except ValueError:
        print("输入必须是数字!")

#add-to-comprehension
def demonstrate_file_modes():   #探讨文件打开模式
    """展示不同文件打开模式的使用"""
    filename = "test_modes.txt"

    # 1. 写入模式 'w'
    print("\n1. 写入模式 'w':")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("第一行内容\n")
        print("文件已创建并写入")

    # 2. 追加模式 'a'
    print("\n2. 追加模式 'a':")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("追加的内容\n")
        print("内容已追加")

    # 3. 读取模式 'r'
    print("\n3. 读取模式 'r':")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"文件内容: {content}")

    # 4. 读写模式 'r+'
    print("\n4. 读写模式 'r+':")
    with open(filename, 'r+', encoding='utf-8') as f:
        existing = f.read()
        f.seek(0)  # 回到文件开头
        f.write("新的第一行\n" + existing)
        print("文件已更新")

    # 5. 二进制模式示例 'rb'
    print("\n5. 二进制模式 'rb':")
    with open(filename, 'rb') as f:
        binary_content = f.read()
        print(f"二进制内容: {binary_content}")

def cleanup():
    """清理测试文件"""
    files_to_remove = ["test_file.txt", "test_pickle.pkl", "test_file1.txt", "test_modes.txt"]
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)


# 基本模式：
'r'  # 只读模式（默认模式）。文件必须存在，否则报错
'w'  # 写入模式。如果文件存在则覆盖，不存在则创建
'a'  # 追加模式。如果文件存在则在末尾追加，不存在则创建
'x'  # 独占创建模式。如果文件已存在则报错，不存在则创建新文件
# 扩展模式（在基本模式后添加）：
'b'  # 二进制模式
't'  # 文本模式（默认）
'+'  # 读写模式
# 常见组合模式：
'rb'   # 二进制只读
'r+'   # 读写模式，从文件开头开始
'rb+'  # 二进制读写
'wb'   # 二进制写入
'w+'   # 读写模式，覆盖已有文件
'wb+'  # 二进制读写，覆盖已有文件
'ab'   # 二进制追加
'a+'   # 读写模式，追加
'ab+'  # 二进制读写，追加



def main():
    print("Python输入输出综合示例程序")
    print("=" * 50)

    demonstrate_output_formatting()
    demonstrate_file_operations()
    demonstrate_pickle_operations()
    demonstrate_input_operations()

    #add-to-comprehension
    demonstrate_file_modes()

    print("\n程序执行完毕, 清理测试文件...")
    cleanup()


if __name__ == "__main__":
    main()