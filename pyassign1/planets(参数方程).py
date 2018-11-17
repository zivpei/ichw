import turtle
import math

# 此处采用参数方程画椭圆轨迹，优点是单变量，处理起来方便；缺点则是周期比例难以精确控制

def move(turtle, a, b, t):
    c = a**2 - b**2
    c = math.sqrt(c)
    turtle.goto(
        a *
        math.cos(
            math.radians(t)) -
        c,
        b *
        math.sin(
            math.radians(t)))
    turtle.pendown()


colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray", "brown", "sea green"]
planets = []
# 或者在planets中先预放6个字符串，然后才再for循环中将它们重新定义为乌龟！
for i in range(6):
    a = turtle.Turtle()
    a.shape("circle")
    a.shapesize((0.1 + i / 10))
    a.color(colors[i])
    a.speed(7 - i)
    # penup()是必要的，否则会在第一次goto时留下痕迹
    a.penup()
    planets.append(a)

wn = turtle.Screen()
wn.bgcolor("black")

sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(0.6)
sun.color(colors[6])

for i in range(3600):
    move(planets[0], 20, 15, 8 * i)
    move(planets[1], 25, 18.75, 7 * i)
    move(planets[2], 30, 22.5, 6 * i)
    move(planets[3], 50, 37.5, 5 * i)
    move(planets[4], 80, 60, 4 * i)
    move(planets[5], 120, 90, 3 * i)

wn.exitonclick()
