a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

print("--------------------------")

n = 10
a, b = 0, 1
for i in range(n):
    print(b)
    a, b = b, a + b

def fab(n):
        if n < 1:
            print('输入有误！')
            return -1
        if n == 1 or n == 2:
            return 1
        else:
            return fab(n - 1) + fab(n - 2)
print("---")
print(fab(11))

print("---")
a, b, i = 0, 1, 0
result = [ ]
n = int(input('输入一个大于 0 的整数: '))
while i < n:
    result.append(b)
    a, b = b, a+b
    i += 1
print(result)