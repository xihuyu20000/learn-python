import secrets

def generate_random_color():
    red = secrets.randbelow(256)
    green = secrets.randbelow(256)
    blue = secrets.randbelow(256)
    return red, green, blue

# 生成随机颜色
color = generate_random_color()
print("随机颜色(RGB):", color)