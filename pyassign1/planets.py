import turtle

sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(0.5)
sun.color("white")

s = turtle.Screen()
s.bgcolor((0, 0, 0))

colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray", "brown", "sea green"]

planets_list = []
for i in range(6):
    a = turtle.Turtle()
    a.color(colors[i])
    a.shape("circle")
    a.shapesize(0.1 + i / 10)
    a.penup()
    a.speed(0)
    planets_list.append(a)

G = 6.67259e-11 * 8e5
M = 1.1989e30 / 1e35

# 此处用字典将planet_list中的turtle与其初始数据列表对应
planets_inf = {
    "0": [11.6, 0, 0, 7.43 / 1e6],
    "1": [21.6, 0, 0, 5.44 / 1e6],
    "2": [29.9, 0, 0, 4.63 / 1e6],
    "3": [45.6, 0, 0, 3.75 / 1e6],
    "4": [155.7, 0, 0, 2.03 / 1e6],
    "5": [285.9, 0, 0, 1.50 / 1e6],
}

# 力学模拟的优点是接近真实模型，但缺点是dt不能取得很大，否则会有明显的“进洞”，
# 本质上这只是一种局部线性近似“拼接”出的轨道模型


def mechanics_model(x, y, vx, vy):
    "微元法画行星轨道的函数"
    dt = 60 * 3600
    ax = -G * M * x / ((x ** 2 + y ** 2) ** 1.5)
    ay = -G * M * y / ((x ** 2 + y ** 2) ** 1.5)
    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x + vx * dt
    y = y + vy * dt
    # 注意返回值可以是多个！
    return x, y, vx, vy


Active = True
while Active:
    for key, value in planets_inf.items():
        x = value[0]
        y = value[1]
        if (x ** 2 + y ** 2) ** 0.5 <= 1:
            # 此处用break并不能跳出while循环（因此如果6个行星同时撞太阳的话，系统仍在不断运行从而陷入死循环！）
            Active = False
        else:
            # 此步为了实现迭代
            value[0], value[1], value[2], value[3] = mechanics_model(
                value[0], value[1], value[2], value[3])
            w = int(key)
            t = planets_list[w]
            t.goto(value[0], value[1])
            t.pendown()

s.exitonclick()
