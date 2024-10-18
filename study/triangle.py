import math


def demonstrate_trig_functions():
    print("Python 三角函数演示\n")

    # 1. math.acos(x) - 反余弦函数
    print("1. math.acos(x) - 反余弦函数")
    x = 0.5
    result = math.acos(x)
    print(f"   math.acos({x}) = {result} 弧度 = {math.degrees(result)} 度")
    print("   用途: 计算三角形的角度")
    a, b, c = 3, 4, 5
    cos_A = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    angle_A = math.acos(cos_A)
    print(f"   三角形(3,4,5)的角A是: {math.degrees(angle_A):.2f} 度\n")

    # 2. math.asin(x) - 反正弦函数
    print("2. math.asin(x) - 反正弦函数")
    x = 0.5
    result = math.asin(x)
    print(f"   math.asin({x}) = {result} 弧度 = {math.degrees(result)} 度")
    print("   用途: 计算正弦值已知的角度")
    sin_value = 0.8660254
    angle = math.asin(sin_value)
    print(f"   正弦值为{sin_value}的角度是: {math.degrees(angle):.2f} 度\n")  #:.2f是指格式化字符串

    # 3. math.atan(x) - 反正切函数
    print("3. math.atan(x) - 反正切函数")
    x = 1
    result = math.atan(x)
    print(f"   math.atan({x}) = {result} 弧度 = {math.degrees(result)} 度")
    print("   用途: 计算斜率对应的角度")
    slope = 0.5
    angle = math.atan(slope)
    print(f"   斜率为{slope}的直线与x轴的夹角是: {math.degrees(angle):.2f} 度\n")

    # 4. math.atan2(y, x) - 二参数反正切函数
    print("4. math.atan2(y, x) - 二参数反正切函数")
    x, y = 1, 1
    result = math.atan2(y, x)
    print(f"   math.atan2({y}, {x}) = {result} 弧度 = {math.degrees(result)} 度")
    print("   用途: 计算向量的方向")
    vector_x, vector_y = -3, 4
    direction = math.atan2(vector_y, vector_x)
    print(f"   向量({vector_x}, {vector_y})的方向是: {math.degrees(direction):.2f} 度\n")

    # 5. math.cos(x) - 余弦函数
    print("5. math.cos(x) - 余弦函数")
    angle_deg = 60
    angle_rad = math.radians(angle_deg)
    result = math.cos(angle_rad)
    print(f"   math.cos({angle_deg}°) = {result}")
    print("   用途: 计算三角形的边长")
    a, b = 3, 4
    angle_C = math.radians(60)
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle_C))
    print(f"   三角形两边长为3和4，夹角60°，第三边的长度是: {c:.2f}\n")

    # 6. math.hypot(x, y) - 计算直角三角形斜边长度
    print("6. math.hypot(x, y) - 计算直角三角形斜边长度")
    x, y = 3, 4
    result = math.hypot(x, y)
    print(f"   math.hypot({x}, {y}) = {result}")
    print("   用途: 计算二维向量的模长")
    vector_x, vector_y = 5, 12
    magnitude = math.hypot(vector_x, vector_y)
    print(f"   向量({vector_x}, {vector_y})的模长是: {magnitude}\n")

    # 7. math.sin(x) - 正弦函数
    print("7. math.sin(x) - 正弦函数")
    angle_deg = 30
    angle_rad = math.radians(angle_deg)
    result = math.sin(angle_rad)
    print(f"   math.sin({angle_deg}°) = {result}")
    print("   用途: 计算三角形的高")
    base = 10
    angle = math.radians(45)
    height = base * math.sin(angle)
    print(f"   底边为10，对应角为45°的三角形，其高是: {height:.2f}\n")

    # 8. math.tan(x) - 正切函数
    print("8. math.tan(x) - 正切函数")
    angle_deg = 45
    angle_rad = math.radians(angle_deg)
    result = math.tan(angle_rad)
    print(f"   math.tan({angle_deg}°) = {result}")
    print("   用途: 计算直线斜率")
    angle = math.radians(30)
    slope = math.tan(angle)
    print(f"   倾角为30°的直线斜率是: {slope:.4f}\n")

    # 9. math.degrees(x) - 弧度转角度
    print("9. math.degrees(x) - 弧度转角度")
    rad = math.pi / 2
    deg = math.degrees(rad)
    print(f"   math.degrees({rad}) = {deg}")
    print("   用途: 将弧度计算结果转换为更易理解的角度")
    result_rad = math.asin(0.5)
    result_deg = math.degrees(result_rad)
    print(f"   arcsin(0.5) = {result_deg:.2f}°\n")

    # 10. math.radians(x) - 角度转弧度
    print("10. math.radians(x) - 角度转弧度")
    deg = 90
    rad = math.radians(deg)
    print(f"   math.radians({deg}) = {rad}")
    print("   用途: 将用户输入的角度转换为弧度以用于计算")
    user_angle = 60
    sin_value = math.sin(math.radians(user_angle))
    print(f"   {user_angle}°的正弦值是: {sin_value:.4f}")


if __name__ == "__main__":
    demonstrate_trig_functions()


