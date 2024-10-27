#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python标准库综合使用示例
展示Python主要标准库的高级用法和完整功能
"""

import os
import sys
import time
import datetime
import random
import math
import re
import json
import urllib.request
import urllib.parse
import glob
import zlib
import logging
import argparse
from pathlib import Path
from collections import Counter, defaultdict
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
import unittest
import doctest

# 配置日志
# basicConfig 函数用于配置日志记录器的基本设置
#可用参数有：level, format, datefmt, filename, filemode, stream
# 这里的level表示日志级别
# 这里的format表示格式化字符串，{levelname}表示日志级别，{asctime}表示时间，{message}表示日志消息,相关参数有：asctime, datefmt, filename, funcName, lineno, levelname, message, module, msecs, name, pathname, process, processName, relativeCreated, thread, threadName

# 日志级别为INFO，日志格式为时间戳+级别+消息
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)    # 创建一个名为__name__的日志记录器
#getLogger 函数用于创建一个日志记录器对象
#有关log的命令
logger.info('=== LOGGING模块操作示例 ===')
logging.debug('这是一条调试信息')
logging.info('这是一条信息')
logging.warning('这是一条警告信息')
logging.error('这是一条错误信息')
logging.critical('这是一条严重错误信息')
logger.info('=== 日志模块操作示例结束 ===\n')

# 配置日志文件
# 这里的filename表示日志文件的路径，filemode表示文件模式，默认为'a'，表示追加模式，如果设置为'w'，则表示覆盖模式
# 这里的stream表示输出流，默认为sys.stdout，即标准输出流，如果设置为sys.stderr，则表示标准错误流

# 配置日志级别
# 这里的level表示日志级别，有几个值：   DEBUG, INFO, WARNING, ERROR, CRITICAL，输出的内容类型分别是   调试  信息  警告  错误  严重错误
# 这里的stream表示输出流，默认为sys.stdout，即标准输出流，如果设置为sys.stderr，则表示标准错误流



class FileSystemDemo:
    """文件系统操作示例类"""

    def __init__(self, base_dir="."):
        """
        初始化示例类
        参数:
            base_dir: 基础目录路径，默认为当前目录
        """
        self.base_dir = Path(base_dir)  #Path类表示路径，这里的base_dir表示基础目录路径

    def demonstrate_os_operations(self):    #self表示当前对象
        """演示os模块的主要操作"""
        logger.info("=== OS模块操作示例 ===")

        # 获取当前工作目录
        current_dir = os.getcwd()
        logger.info(f"当前工作目录: {current_dir}")

        # 创建目录
        test_dir = self.base_dir / "test_dir"    # 拼接路径
        os.makedirs(test_dir, exist_ok=True)    #exist_ok=True表示如果目录已经存在，则不会抛出异常
        logger.info(f"创建目录: {test_dir}")

        # 列出目录内容
        logger.info(f"当前目录内容: \n{os.listdir(self.base_dir)}")
        logger.info(f"新建目录下的文件: \n{os.listdir(test_dir)}")

        # 获取文件信息
        file_stat = os.stat(__file__)    #os.stat()函数用于获取文件信息，这里的__file__表示当前文件的路径
        logger.info(f"当前文件信息:\n"
                    f"大小: {file_stat.st_size} 字节\n"    #st_size表示文件大小，单位为字节
                    f"创建时间: {datetime.datetime.fromtimestamp(file_stat.st_ctime)}\n"    #st_ctime表示文件创建时间，单位为秒   英文：create
                    f"最后修改时间: {datetime.datetime.fromtimestamp(file_stat.st_mtime)}")    #st_mtime表示文件最后修改时间，单位为秒  英文：modify

        # 使用 glob 进行文件匹配
        py_files = glob.glob("*.py")    #glob.glob()函数用于匹配文件路径，这里的*.py表示匹配所有以.py结尾的文件
        logger.info(f"当前目录下的Python文件: {py_files}")


class DateTimeDemo:
    """日期时间处理示例类"""

    def demonstrate_datetime_operations(self):
        """演示datetime模块的主要操作"""
        logger.info("\n=== DateTime模块操作示例 ===")

        # 获取当前时间
        now = datetime.datetime.now()    #datetime.datetime.now()函数用于获取当前时间
        logger.info(f"当前时间: {now}")

        # 时间格式化
        formatted = now.strftime("%Y年%m月%d日 %H时%M分%S秒")    #strftime()函数用于格式化时间，这里的%Y表示年，%m表示月，%d表示日，%H表示时，%M表示分，%S表示秒
        #如果使用%M作为月，
        logger.info(f"格式化后的时间: {formatted}")
        #用%D输出
        logger.info(f"用strftime-%D输出的时间: {now.strftime("%D")}")

        # 时间计算
        #datetime模块的timedelta类表示时间间隔.参数有：days, seconds, microseconds, milliseconds, minutes, hours, weeks
        #这里的days表示天数，seconds表示秒数，microseconds表示微秒数，milliseconds表示毫秒数，minutes表示分钟数，hours表示小时数，weeks表示周数
        future = now + datetime.timedelta(days=30, hours=12)
        logger.info(f"30天12小时后: {future}")

        # 解析时间字符串
        date_str = "2024-12-31 23:59:59"
        #被解析的字符串格式可以是：%Y-%m-%d %H:%M:%S, %Y-%m-%d %H:%M:%S.%f   .%f是微秒
        parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        logger.info(f"解析的时间: {parsed_date}")

        # 计算时间差
        time_diff = future - now
        logger.info(f"时间差: {time_diff.days}天 {time_diff.seconds // 3600}小时")
        # 运行时间差
        logger.info(f"运行时间差: {datetime.datetime.now()-now}")


class StringProcessingDemo:
    """字符串处理示例类"""

    def demonstrate_string_operations(self):
        """演示字符串处理相关操作"""
        logger.info("\n=== 字符串处理示例 ===")

        # 正则表达式示例
        text = "我的邮箱是 example@email.com，电话是 13812345678"

        # 提取邮箱
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'    # 正则表达式
        #r前缀表示原始字符串，\b表示单词边界,[A-Za-z0-9._%+-]表示匹配字母(大写字母、小写字母)、数字、下划线、百分号、加号、减号、点。+表示匹配一次或多次，前面的+是表示[A-Za-z0-9._%+-]匹配一次或多次，后面的+是表示[0-9]匹配一次或多次。
        #\.表示匹配点，[A-Z|a-z]表示匹配字母，|表示或，{2,}表示匹配2个或以上
        #\b作用是匹配单词边界，即单词的开头或结尾。
        email = re.findall(email_pattern, text)
        logger.info(f"提取的邮箱: {email}")

        # 提取手机号
        phone_pattern = r'1[3-9]\d{9}'
        # 1[3-9]表示匹配以1开头，后面跟着3-9中的一个数字，\d{9}表示匹配9个数字
        phone = re.findall(phone_pattern, text)
        logger.info(f"提取的手机号: {phone}")

        # 字符串替换
        masked_text = re.sub(phone_pattern, '***********', text)
        #re.sub()函数用于替换字符串中的匹配项，这里的text表示要替换的字符串，phone_pattern表示要替换的模式，'***********'表示替换后的字符串
        logger.info(f"隐藏手机号后的文本: {masked_text}")


class NetworkDemo:
    """网络操作示例类"""

    def demonstrate_network_operations(self):
        """演示网络相关操作"""
        logger.info("\n=== 网络操作示例 ===")
        #urlib是一个Python标准库，用于处理URL。
        # GET请求示例
        def make_get_request(url):
            try:
                #urllib.request.urlopen()函数用于打开一个URL，返回一个响应对象
                with urllib.request.urlopen(url) as response:   #as是关键字，表示with语句的上下文管理器，response表示响应对象
                    #response.read()表示读取响应内容，response.read().decode('utf-8')表示将响应内容解码为字符串
                    return response.read().decode('utf-8')
            except Exception as e:
                logger.error(f"请求失败: {e}")
                return None
        #with语句：应用在需要打开、处理和关闭资源的场景，with语句会自动处理资源的打开和关闭，避免了手动关闭资源的繁琐操作。

        # POST请求示例
        def make_post_request(url, data):
            try:
                #urllib.parse.urlencode()函数用于将字典转换为URL编码的字符串，data表示要编码的字典
                data = urllib.parse.urlencode(data).encode('utf-8') #encode('utf-8')表示将字符串编码为UTF-8格式
                #data结果：b'name=%E5%BC%A0%E4%B8%89&age=25'
                #urllib.request.Request()函数用于创建一个请求对象，url表示请求的URL，data表示请求的数据，method表示请求的方法，默认为GET
                req = urllib.request.Request(url, data=data, method='POST')
                with urllib.request.urlopen(req) as response:   #urlopen()函数可接受url(get)或请求对象(post)
                    return response.read().decode('utf-8')  #decode('utf-8')表示将响应内容解码为字符串
            except Exception as e:
                logger.error(f"请求失败: {e}")
                return None
        #Get/Post：
        #Get：获取资源，Post：提交数据
        #Get：请求参数在URL中，Post：请求参数在请求体中
        # 示例URL（使用httpbin进行测试）
        get_url = "http://httpbin.org/get"    # 示例URL（使用httpbin进行测试）
        post_url = "http://httpbin.org/post"    # 示例URL（使用httpbin进行测试）
        #httpbin是一个测试网站，用于测试HTTP请求和响应

        # 发送GET请求
        logger.info("发送GET请求...")
        get_response = make_get_request(get_url)
        if get_response:
            logger.info(f"GET响应: {get_response[:1000]}")  #[:1000]指的是取前1000个字符

        # 发送POST请求
        post_data = {
            'name': '张三',
            'age': 25
        }
        logger.info("发送POST请求...")
        post_response = make_post_request(post_url, post_data)
        if post_response:
            logger.info(f"POST响应: {post_response}")


class MathDemo:
    """数学计算示例类"""

    def demonstrate_math_operations(self):
        """演示数学相关操作"""
        logger.info("\n=== 数学运算示例 ===")

        # 基本数学运算
        logger.info(f"π值: {math.pi}")
        logger.info(f"e值: {math.e}")
        logger.info(f"2的平方根: {math.sqrt(2)}")
        logger.info(f"2的10次方: {math.pow(2, 10)}")

        # 三角函数
        angle = math.pi / 6  # 30度
        logger.info(f"cos(45°): {math.cos(angle)}")
        logger.info(f"sin(45°): {math.sin(angle)}")
        # 指数函数
        logger.info(f"e的2次方: {math.exp(2)}")

        # 对数函数
        logger.info(f"以e为底的2的对数: {math.log(2)}")
        logger.info(f"以10为底的100的对数: {math.log10(100)}")

        # 舍入函数
        logger.info(f"向上取整: {math.ceil(3.14)}")
        logger.info(f"向下取整: {math.floor(3.14)}")
        logger.info(f"四舍五入: {round(3.14)}")

        # 绝对值
        logger.info(f"绝对值: {math.fabs(-5)}")

        #random模块介绍：
        #random模块是Python标准库中的一个模块，用于生成随机数。
        #random模块提供了以下功能：
        #生成随机整数 random.randint(1, 100)
        #生成随机浮点数    random.random() 范围为0到1
        #从序列中随机选择一个元素   random.choice(items)
        #从序列中随机选择多个元素  random.sample(items, 3)


        # 随机数种子
        random.seed(42)    #random.seed()函数用于设置随机数生成器的种子，42表示种子值
        # 随机数生成
        logger.info("\n随机数示例:")
        logger.info(f"随机整数(1-100): {random.randint(1, 100)}")
        logger.info(f"随机浮点数(0-1): {random.random():.3f}")   #取前三位浮点数：{random.random():.3f}

        # 随机选择
        items = ['苹果', '香蕉', '橘子', '葡萄']
        logger.info(f"随机选择: {random.choice(items)}")    #random.choice()函数用于从给定的序列中随机选择一个元素，items表示序列
        logger.info(f"随机采样(取3个): {random.sample(items, 3)}")    #random.sample()函数用于从给定的序列中随机选择指定数量的元素，items表示序列，3表示数量


class CompressionDemo:
    """数据压缩示例类"""

    def demonstrate_compression(self):
        """演示数据压缩相关操作"""
        logger.info("\n=== 数据压缩示例 ===")

        # 字符串压缩
        text = "这是一个需要压缩的很长的字符串" * 100
        text_bytes = text.encode('utf-8')   #如果不encode('utf-8')，text类型是str类型，而encode('utf-8')是将str类型转换为bytes类型
        #bytes类型是字节序列，每个字节都是一个整数，范围是0到255，即0x00到0xFF。转为bytes类型的原因是，Python中的字符串都是以Unicode编码的，Unicode占用2个字节。
        #Unicode编码，范围是0x0000到0
        #zlib.compress()函数用于压缩数据，text_bytes表示要压缩的数据需要类型是bytes类型，text类型是str类型，需要encode('utf-8')转换为bytes类型
        #compressed类型是bytes类型
        #zlib模块是Python标准库，用于数据压缩和解压缩。

        # 压缩
        compressed = zlib.compress(text_bytes)  #zlib.compress()函数用于压缩数据，text_bytes表示要压缩的数据，compressed类型是bytes类型
        logger.info(f"compressd的类型是：{type(compressed)}")
        logger.info(f"原始大小: {len(text_bytes)} 字节")
        logger.info(f"压缩后大小: {len(compressed)} 字节")
        logger.info(f"压缩率: {(1 - len(compressed) / len(text_bytes)) * 100:.2f}%")

        # 解压缩
        decompressed = zlib.decompress(compressed)
        logger.info(f"解压后大小: {len(decompressed)} 字节")
        logger.info(f"解压后内容与原始内容相同: {decompressed == text_bytes}")


class TestDemo(unittest.TestCase):    #unittest.TestCase是unittest框架中的一个类，用于编写单元测试用例
    """单元测试示例类"""

    def setUp(self):
        """测试准备"""
        self.math_demo = MathDemo()

    def test_math_operations(self):
        """测试数学运算"""
        logger.info("\n=== 测试数学运算 ===")
        logger.info("测试cos(45°)")
        logger.info(f"cos(45°) = {math.cos(math.pi / 4)}")

        logger.info(f"cos(45°) = 0.7071067811865476 \t{self.assertAlmostEqual(math.cos(math.pi / 4), 0.7071067811865476)}")
        #返回的是None，因为assertAlmostEqual()函数没有返回值，只有断言失败时才会抛出异常
        self.assertEqual(math.pow(2, 10), 1024)

    def test_random_operations(self):
        """测试随机数操作"""
        random_int = random.randint(1, 100)
        self.assertTrue(1 <= random_int <= 100)

    #断言判断示例
    def test_assert_operations(self):
        """测试断言操作"""
        with self.assertRaises(ValueError):
            int("abc")
        #self.assertRaises()函数用于断言一个函数或方法是否会抛出指定的异常，ValueError表示要断言的异常类型
        #int("abc")表示将字符串"abc"转换为整数，int()函数会抛出ValueError异常，然后assertRaises()函数会捕获这个异常并断言它的类型是否为ValueError
        #然后判断确实为ValueError异常，然后断言通过
        #断言不通过示例 if 1:
        if 0:
            int("ABC")

    def tearDown(self):
        """测试清理"""    #tearDown()函数用于清理测试环境，del self.math_demo表示删除self.math_demo对象
        #清理测试环境作用是为了保证测试环境的稳定性，防止测试用例之间的干扰
        del self.math_demo



def main():
    """主函数"""
    try:
        # 创建示例对象
        fs_demo = FileSystemDemo()
        dt_demo = DateTimeDemo()
        str_demo = StringProcessingDemo()
        net_demo = NetworkDemo()
        math_demo = MathDemo()
        comp_demo = CompressionDemo()

        # 运行演示
        fs_demo.demonstrate_os_operations()
        dt_demo.demonstrate_datetime_operations()
        str_demo.demonstrate_string_operations()
        net_demo.demonstrate_network_operations()
        math_demo.demonstrate_math_operations()
        comp_demo.demonstrate_compression()

        # 运行单元测试
        logger.info("\n=== 运行单元测试 ===")
        unittest.main(argv=['dummy'])    #unittest.main()函数用于运行单元测试，argv=['dummy']表示传递一个空的参数列表给unittest.main()函数
        #这个函数会调用所有继承自unittest.TestCase的类中的test开头的方法，运行这些方法中的测试用例。
        #这个地方也可以是unittest.main()，里面留空，表示运行所有的测试用例。
    except Exception as e:
        logger.error(f"程序运行出错: {e}")
        sys.exit(1)
    finally:
        logger.info("\n=== 程序结束 ===")


if __name__ == "__main__":
    main()