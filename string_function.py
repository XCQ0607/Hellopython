
def print_separator(title):
    print(f"\n{'-'*20} {title} {'-'*20}")

# 测试字符串
test_string = "Hello, World! This is a Test String. 123"
print_separator("原始字符串")
print(f"原始字符串: '{test_string}'")

# 1. capitalize()   #将字符串的第一个字符转换为大写
print_separator("capitalize()")
print(f"capitalize(): '{test_string.capitalize()}'")

# 2. center()   #返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print_separator("center()")
print(f"center(50, '*'): '{test_string.center(50, '*')}'")

# 3. count()    #返回 str 在 string 里面出现的次数，如果 beg（start） 或者 end 指定则返回指定范围内 str 出现的次数
print_separator("count()")
print(f"count('i'): {test_string.count('i')}")
print(f"count('i', 10, 20): {test_string.count('i', 10, 20)}")

# 4 & 5. encode() 和 decode()    #以 encoding 指定的编码格式编码字符串
print_separator("encode() 和 decode()")
encoded = test_string.encode('utf-8')
print(f"encode('utf-8'): {encoded}")
print(f"decode('utf-8'): {encoded.decode('utf-8')}")    #decode('utf-8') 是将使用 UTF-8 编码的字节序列转换回原始的 Unicode 字符串。

# 6. endswith()     #检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。
print_separator("endswith()")
print(f"endswith('123'): {test_string.endswith('123')}")
print(f"endswith('World', 0, 12): {test_string.endswith('World', 0, 12)}")

# 7. expandtabs()   #把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8
print_separator("expandtabs()")
tabbed_string = "Hello\tWorld"
print(f"原始: '{tabbed_string}', expandtabs(4): '{tabbed_string.expandtabs(4)}'")

# 8 & 9. find() 和 index()       #检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
print_separator("find() 和 index()")
print(f"find('World'): {test_string.find('World')}")
print(f"index('World'): {test_string.index('World')}")  #跟find()方法一样，只不过如果str不在字符串中会报一个异常。

# 10-17. is...() 方法
Arabic = "١٢٣"
print_separator("is...() 方法")
print(f"isdecimal(): {test_string.isdecimal()}")    #检查字符串是否只包含十进制字符（十进制字符是指从0到9的数字字符，不包括阿拉伯数字），如果是返回 True，否则返回 False。
print(f"isidentifier(): {test_string.isidentifier()}")    #检查字符串是否是有效的标识符，如果是返回 True，否则返回 False。
print(f"isnumeric(): {test_string.isnumeric()}")    #检查字符串是否只包含数字字符，如果是返回 True，否则返回 False。
print(f"isalnum(): {test_string.isalnum()}")    #检查字符串是否由字母和数字组成，即字符串中的所有字符都是字母或数字。如果字符串至少有一个字符，并且所有字符都是字母或数字，则返回 True；否则返回 False。
print(f"isalpha(): {test_string.isalpha()}")    #如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
print(f"isdigit(): {test_string.isdigit()}")    #如果字符串只包含数字则返回 True 否则返回 False..
print(f"isdigit()--阿拉伯数字: {Arabic.isdigit()}")    #如果字符串只包含数字(包括阿拉伯数字)则返回 True 否则返回 False.
print(f"isprintable(): {test_string.isprintable()}")    #如果字符串中的所有字符都是可打印的或字符串为空，则返回 True，否则返回 False。
print(f"islower(): {test_string.islower()}")    #如果字符串中只有小写字符，则返回 True，否则返回 False。
print(f"isspace(): {test_string.isspace()}")    #如果字符串中只包含空格，则返回 True，否则返回 False。
print(f"istitle(): {test_string.istitle()}")    #如果字符串是标题化的（每个单词的首字母大写）则返回 True，否则返回 False。
print(f"isupper(): {test_string.isupper()}")    #如果字符串中全部是大写字符，则返回 True，否则返回 False。


# 18. join()    #将序列中的元素以指定的字符连接生成一个新的字符串
print_separator("join()")
words = ["Hello", "World", "Python"]
print(f"' '.join(['Hello', 'World', 'Python']): '{' '.join(words)}'")
#类似于方法append()
words.append('000')
print(f"words.append(['000']): {words}")
#错误示例：print(f"words.append(['000']): {words.append('000')}")
# append() 方法用于在列表末尾添加一个元素。它直接修改原列表，不返回新的列表。
# append() 方法的返回值是 None。这是因为该方法在原地修改列表，而不是创建并返回新的列表。
# join() 方法返回一个新的字符串，该字符串是通过将序列中的元素连接起来而形成的。
# 当你打印 append() 的结果时，你实际上是在打印 None

# 19. len()   #返回字符串的长度
print_separator("len()")
print(f"len(): {len(test_string)}")

# 20. ljust()     #返回一个原字符串左对齐,并默认使用空格填充至长度 width 的新字符串
print_separator("ljust()")
print(f"ljust(50, '*'): '{test_string.ljust(50, '*')}'")

# 21. lower()     #转换字符串中所有大写字符为小写
print_separator("lower()")
print(f"lower(): '{test_string.lower()}'")

# 22. lstrip()    #截掉字符串左边的空格或指定字符
print_separator("lstrip()")
print(f"lstrip(): '{test_string.lstrip('Hello')}'")

# 23. maketrans() 和 translate()
print_separator("maketrans() 和 translate()")
trans_table = str.maketrans("aeiou", "12345")
print(f"translate(maketrans('aeiou', '12345')): '{test_string.translate(trans_table)}'")

# 24 & 25. max() 和 min()
print_separator("max() 和 min()")
print(f"max(): '{max(test_string)}'")
print(f"min(): '{min(test_string)}'")

# 26. replace()
print_separator("replace()")
print(f"replace('World', 'Python'): '{test_string.replace('World', 'Python')}'")

# 27 & 28. rfind() 和 rindex()
print_separator("rfind() 和 rindex()")
print(f"rfind('i'): {test_string.rfind('i')}")
print(f"rindex('i'): {test_string.rindex('i')}")

# 29. rjust()
print_separator("rjust()")
print(f"rjust(50, '*'): '{test_string.rjust(50, '*')}'")

# 30. rstrip()
print_separator("rstrip()")
print(f"rstrip(): '{test_string.rstrip()}'")

# 31. split()
print_separator("split()")
print(f"split(): {test_string.split()}")
print(f"split(', '): {test_string.split(', ')}")

# 32. splitlines()
print_separator("splitlines()")
multiline = "Line 1\nLine 2\nLine 3"
print(f"splitlines(): {multiline.splitlines()}")

# 33. startswith()
print_separator("startswith()")
print(f"startswith('Hello'): {test_string.startswith('Hello')}")

# 34. strip()
print_separator("strip()")
print(f"strip(): '{test_string.strip()}'")

# 35. swapcase()
print_separator("swapcase()")
print(f"swapcase(): '{test_string.swapcase()}'")

# 36. title()
print_separator("title()")
print(f"title(): '{test_string.title()}'")

# 38. upper()
print_separator("upper()")
print(f"upper(): '{test_string.upper()}'")

# 39. zfill()
print_separator("zfill()")
number = "42"
print(f"zfill(5): '{number.zfill(5)}'")

# 40. isdecimal()
print_separator("isdecimal()")
print(f"isdecimal(): {test_string.isdecimal()}")
print(f"isdecimal(): {'123'.isdecimal()}")

# 41. removeprefix()    # 移除字符串前缀
print_separator("removeprefix()")
print(f"removeprefix('Hello'): '{test_string.removeprefix('Hello')}'")