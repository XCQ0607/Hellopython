import logging
import sys
import traceback
import time
import os

# 配置日志
logging.basicConfig(level=logging.DEBUG)  # 设置日志级别为DEBUG


# 日志等级
# +-- DEBUG：详细的调试信息，通常用于调试过程中。
# +-- INFO：重要信息，通常用于记录程序的运行状态。
# +-- WARNING：警告信息，通常用于非关键问题。
# +-- ERROR：错误信息，通常用于记录程序运行过程中出现的错误。
# +-- CRITICAL：严重错误信息，通常用于记录程序运行过程中出现的严重错误。
# +-- FATAL：致命错误信息，通常用于记录程序运行过程中出现的致命错误。
# +-- NOTSET：未设置日志级别，通常用于禁用日志记录。


# 自定义异常类
class CustomError(Exception):
    """自定义的异常类"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# 异常类型树
"""
BaseException
 +-- SystemExit (退出程序)
 +-- KeyboardInterrupt  (键盘中断)
 +-- GeneratorExit    (生成器退出)
 +-- Exception    (所有异常的基类)
      +-- StopIteration (迭代器没有更多元素)
      +-- ArithmeticError    (算术错误)
      |    +-- FloatingPointError    (浮点运算错误)
      |    +-- OverflowError      (溢出错误)
      |    +-- ZeroDivisionError    (除零错误)
      +-- AssertionError      (断言错误)
      +-- AttributeError      (属性错误)
      +-- BufferError     (缓冲区错误)
      +-- EOFError        (文件结束)
      +-- ImportError     (导入模块错误)
      +-- LookupError     (查找错误)
      |    +-- IndexError    (索引错误)
      |    +-- KeyError      (键错误)
      +-- MemoryError     (内存错误)
      +-- NameError       (名称错误)
      +-- OSError         (操作系统错误)
      |    +-- FileExistsError        (文件已存在)
      |    +-- FileNotFoundError    (文件未找到)
      |    +-- PermissionError    (权限错误)
      +-- RuntimeError    (运行时错误)
      +-- SyntaxError     (语法错误)
      +-- SystemError     (系统错误)
      +-- TypeError       (类型错误)
      +-- ValueError      (值错误)
      +-- CustomError (自定义异常)
      
      +-- InterruptedError (中断错误)
      +-- IndexError (索引错误)
      +-- KeyError (键错误)
      +-- IndentationError (缩进错误)
"""


def divide(x, y):
    """
    除法函数,演示异常处理
    """
    try:
        result = x / y
    except ZeroDivisionError:
        # 除数为0异常
        logging.error("除数不能为0!")
        raise  # 抛出异常
    except TypeError:
        # 类型错误异常
        logging.error("参数必须是数字!")
        raise
    else:
        logging.info(f"除法计算成功: {x} / {y} = {result}")
        return result
    finally:    # 无论是否发生异常都会执行
        logging.debug("divide函数执行完毕")


def read_file(filename):
    """
    读取文件函数,演示文件操作异常处理
    """

    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        # 文件不存在异常
        logging.error(f"文件 {filename} 不存在!")
        raise
        # 权限不足异常
        logging.error(f"没有权限读取文件 {filename}!")
        raise
    except IOError as e:      # 捕获所有IO异常
        # IO异常,指的是输入输出错误,如文件不存在、磁盘已满、网络连接失败等
        logging.error(f"读取文件 {filename} 时发生IO错误: {str(e)}")
        raise
    else:     # 没有异常时执行
        logging.info(f"成功读取文件 {filename}")
        return content


def complex_operation(x, y, filename):
    """
    复杂操作函数,整合多种异常处理
    """
    try:
        # 调用可能引发异常的函数
        result = divide(x, y)
        logging.info(result)
        # 自定义异常
        if result > 100.0:
            raise CustomError("结果超过100!")
        content = read_file(filename)  # 调用可能引发异常的函数
        # 断言
        assert len(content) > 0, "文件内容为空!"  #断言：如果条件为False，则抛出AssertionError异常
        logging.info("---------------------")
        logging.info(f"{filename}文件内容: \n{content}")
        logging.info("---------------------")

    except (ZeroDivisionError, TypeError) as e: #as e: 捕获多个异常类型
        logging.error(f"数学运算错误: {str(e)}")
    except (FileNotFoundError, PermissionError, IOError) as e:
        logging.error(f"文件操作错误: {str(e)}")
    except CustomError as e:
        logging.error(f"自定义异常: {str(e)}")
    except AssertionError as e:
        logging.error(f"断言错误: {str(e)}")
    except Exception as e:
        # 捕获所有其他异常
        logging.error(f"发生未知异常: {str(e)}")
        logging.error(traceback.format_exc())
    else:
        logging.info("所有操作成功完成")
        return result, content
    finally:
        logging.debug("complex_operation函数执行完毕")


if __name__ == "__main__":
    # 测试各种异常情况
    #设置工作目录为当前文件所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #创建testfile.txt在工作目录下
    with open("test_file.txt", "w") as f:
        f.write("Hello, world!")

    complex_operation(10, 2, "test_file.txt")  # 正常情况
    logging.info("-------------------------")
    complex_operation(10, 0, "example.txt")  # 除零错误
    logging.info("-------------------------")
    complex_operation("10", 2, "example.txt")  # 类型错误
    logging.info("-------------------------")
    complex_operation(10, 2, "nonexistent.txt")  # 文件不存在
    logging.info("-------------------------")
    complex_operation(1000, 2, "example.txt")  # 自定义异常
    logging.info("-------------------------")
    complex_operation(10000, 2, "example.txt")
    logging.info("-------------------------")
    complex_operation(10, 2, "empty.txt")  # 断言错误(假设empty.txt为空文件)

    #清除临时文件
    os.remove("test_file.txt")
    # 捕获键盘中断
    try:
        # 等待5秒
        time.sleep(5)
    except KeyboardInterrupt:  # 当用户按下Ctrl+C时，会抛出KeyboardInterrupt异常
        logging.info("程序被用户中断")

    sys.exit(0)  # 正常退出
