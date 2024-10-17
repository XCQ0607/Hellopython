# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号()，列表使用方括号[]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。


tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
print(r"tup3 = 'a', 'b', 'c', 'd'","---", type(tup3))
tup0 = (5)
tup00 = (5,)
print("tup0 = (5)",type(tup0))
print("tup00 = (5,)",type(tup00))
tup4 = ()    # 空元组
print("tup4 = ()",type(tup4))
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等

#重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象。
print("id(tup1)",id(tup1))
tup1 = (12, 34.56)
print("tup1 = (12, 34.56)","\nid(tup1)",id(tup1))

# 以下修改元组元素操作是非法的。
# tup1[0] = 100
print("-----------------------------")
import collections
User = collections.namedtuple('User', 'name age id')
user = User('XCQ', '18', '202410308224')
print(user)

print("-----------------------------")
from collections import namedtuple
# 定义一个namedtuple类型User，并包含name，sex和age属性。
User = namedtuple('User', ['name', 'sex', 'age'])
# 创建一个User对象
user = User(name='Runoob', sex='male', age=12)
user1 = User(name='user1', sex='male', age=21)
# 获取所有字段名
print( user._fields )
print("-------")
# 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
user0 = User._make(['Runoob', 'male', 12])
print( user0 )
print( user1 )
# User(name='user1', sex='male', age=12)
# 获取用户的属性
print( user.name )
print( user.sex )
print( user.age )
# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print( user )
# 将User对象转换成字典，注意要使用"_asdict"
print( user._asdict() )
# OrderedDict([('name', 'Runoob'), ('sex', 'male'), ('age', 22)])


