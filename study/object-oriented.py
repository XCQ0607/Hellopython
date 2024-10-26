#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#以上内容是为了unix和linux系统下运行
"""
一个全面的Python面向对象编程示例
展示了类的定义、继承、多态、封装等概念
"""


class Animal:
    """动物基类"""

    count = 0  # 类变量,用于记录动物数量

    def __init__(self, name, age):
        """
        构造方法
        :param name: 动物名称
        :param age: 动物年龄
        """
        self.name = name  # 实例变量
        self.age = age  # 实例变量
        Animal.count += 1  # 更新动物数量 #count是类变量，每次创建一个新的Animal对象时，count就会加1

    def speak(self):
        """发出声音(抽象方法)"""
        raise NotImplementedError("子类必须实现这个方法")

    @classmethod    # @classmethod装饰器,将方法转换为类方法
    def get_count(cls):
        """类方法,获取动物数量"""
        return cls.count

    @staticmethod   # @staticmethod装饰器,将方法转换为静态方法
    def info():
        """静态方法,打印信息"""
        print("这是动物类")

    def __str__(self):
        """返回对象的字符串表示"""
        return f"{self.name}是一只{self.age}岁的动物"

    def __repr__(self):
        """返回对象的字符串表示(详细信息)"""
        return f"Animal('{self.name}', {self.age})"


class Dog(Animal):  #Dog类继承自Animal类
    """狗类,继承自动物类"""

    def __init__(self, name, age, breed):
        """
        构造方法
        :param name: 狗的名称
        :param age: 狗的年龄
        :param breed: 狗的品种
        """
        super().__init__(name, age)  # super()调用父类的构造方法
        self.breed = breed

    def speak(self):
        """重写父类的speak方法"""
        return "汪汪!"

    def fetch(self):
        """狗特有的方法"""
        return f"{self.name}在接飞盘"


class Cat(Animal):
    """猫类,继承自动物类"""

    def __init__(self, name, age, color):
        """
        构造方法
        :param name: 猫的名称
        :param age: 猫的年龄
        :param color: 猫的颜色
        """
        # super().__init__(name, age) # super()调用父类的构造方法，也可以写成Animal.__init__(self, name, age)
        Animal.__init__(self, name, age)
        self.color = color

    def speak(self):
        """重写父类的speak方法"""
        return "喵喵!"

    def climb(self):
        """猫特有的方法"""
        return f"{self.name}在爬树"


def animal_speak(animal):   #传入的参数是一个Animal对象
    #多态是指在不同的对象类型上调用相同的方法，产生不同的行为
    """
    多态示例
    :param animal: 动物对象
    """
    print(animal.speak())   # 调用animal对象的speak方法，根据不同的对象类型调用不同的方法


if __name__ == "__main__":
    # 创建动物对象
    dog = Dog("旺财", 3, "金毛")
    cat = Cat("咪咪", 2, "橘色")

    # 使用对象方法
    print(dog)  # 调用__str__方法
    print(repr(cat))  # 调用__repr__方法
    print(f"{dog.name}说: {dog.speak()}")
    print(f"{cat.name}说: {cat.speak()}")
    print(dog.fetch())
    print(cat.climb())

    # 多态示例
    print("\n多态示例:")
    for animal in (dog, cat):
        # animal_speak(animal)  # 调用animal_speak函数，传入不同的对象类型
        print(animal.speak())  # 调用animal对象的speak方法，根据不同的对象类型调用不同的方法

    # 使用类方法和静态方法
    print(f"\n总共有{Animal.get_count()}只动物")  # 调用类方法
    Animal.info()    # 调用静态方法

    # 访问类变量
    print(f"Animal.count = {Animal.count}") # 访问类变量

    # 尝试直接调用抽象方法
    try:
        Animal("测试", 1).speak()
    except NotImplementedError as e:
        print(f"\n抽象方法调用失败: {e}")