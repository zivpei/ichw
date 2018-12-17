"""
tile.py
_name_: Liu Xingpei
_pkuid_: 1800011711
_email_: zivpei@pku.edu.cn
"""

import time
import turtle


x, y, z, w, S, s, n = [0 for i in range(7)]
pieces = 0
ans = []


def valid(i, k):
    """数组选择合理性检测函数，分为横铺与竖铺，返回检测结果T/F、列表及横铺/竖铺的判断值"""
    global x, y, z, w, s, S
    if z == 1:
        list1 = []
    else:
        list1 = list(range(x - z + 2, x)) + [0]
    if w == 1:
        list2 = []
    else:
        list2 = list(range(x - w + 2, x)) + [0]
    if k <= S:
        # 竖铺检测, 越界的检测依靠同余思想
        if k - i == x * (z - 1) + w - 1 and i % x not in list2:
            return True, [j for t in range(w - 1, -1, -1)
                          for j in range(i + w - 1 - t, k - t + 1, x)], 1
        # 横铺检测
        if k - i == x * (w - 1) + z - 1 and i % x not in list1:
            return True, [j for t in range(z - 1, -1, -1)
                          for j in range(i + z - 1 - t, k - t + 1, x)], 2
    return False, [0]


def test_if_in(a, l):
    """判断合理的砖块数组是否已经被去除"""
    for j in l:
        if j not in a:
            return False
    return True


def remove(a, l):
    """将合理的砖块数组从待选数组中删除"""
    # 由于是一维列表，浅拷贝可以carry
    b = a[:]
    for j in l:
        if j in b:
            b.remove(j)
    return b


def tile(a, b, total_s=0, cnt=0):
    """递归法实现铺砖过程，并将每一种可行的结果添加到一个列表中"""
    global n, ans, s, S, x, y, z, w
    # 如果已铺面积与墙的面积相等，则将结果添加到答案列表ans中
    if total_s == S:
        ans.append(b[:])
        n = n + 1
    else:
        # 每次取列表中的第一个元素进行横竖铺砖检测
        j = a[0]
        for k in range(j + x * (w - 1) + z - 1, j + x * (z - 1) + w):
            if valid(j, k)[0]:
                d = valid(j, k)[1]
                if test_if_in(a, d):
                    b[cnt] = tuple(d)
                    # 将结果进行传递，思想上与八皇后问题的第一种解法类似
                    tile(remove(a, d), b, total_s + s, cnt + 1)


def main():
    """主程序块"""
    global x, y, z, w, S, s, n, pieces, ans

    x = int(input("Please input the length of the wall:"))
    y = int(input("Please input the width of the wall:"))
    z = int(input("Please input the length of the tile:"))
    w = int(input("Please input the width of the tile:"))
    S = x * y
    s = z * w
    n = 0
    pieces = int(S / s)

    # 先对可铺性进行检验
    if S % s == 0:
        if z < w:
            z, w = w, z

        # 列表b用来储存每一次可行的铺法
        b = [0] * pieces
        # 列表a储存着(x*y)块砖
        a = [i for i in range(1, S + 1)]

        t1 = time.process_time()
        tile(a, b)
        t2 = time.process_time()
        print(ans)
        print("Total plans: ", n)
        # 打印运算时间并保留8位小数
        print("Time:", "%.8f" % (t2 - t1) + "s")
    else:
        print("Error")

    if ans:
        scr = turtle.Screen()
        scr.bgcolor("black")
        scr.colormode(255)
        t = turtle.Turtle()
        wr = turtle.Turtle()
        prompt = "Input number of 0–" + str(n - 1)
        st = int(turtle.numinput("Select plan", prompt, 0, 0, n - 1))
        l = ans[st]
        length = 35
        # 依据用户输入的x、y值修改画布的边界，使得最终呈现的图形居中
        scr.setworldcoordinates(-length * x, -length *
                                (y + x), length * 2 * x, length * x)

        t.penup()
        wr.penup()
        t.speed(0)
        t.pensize(0)
        t.pencolor((119, 66, 141))
        wr.pencolor("white")
        t.setheading(0)
        wr.hideturtle()
        # 首先画网格线并给砖标号
        for i in range(y):
            t.goto(0, -(i + 1) * length)
            t.pendown()
            for j in range(1, x + 1):
                t.forward(length)
                wr.goto(t.xcor() - 0.5 * length, t.ycor() + 0.5 * length)
                wr.write(str(i * x + j), align="center",
                         font=("Arial", 64 // max([x, y]), "normal"))
            t.penup()
        t.setheading(270)
        for i in range(x - 1):
            t.goto((i + 1) * length, 0)
            t.pendown()
            t.forward(y * length)
            t.penup()

        t.pensize(3)
        t.pencolor((255, 177, 27))
        # 给砖块勾边
        for i in l:
            # 将画笔置于砖块的左上角
            if int(i[0] % x) == 0:
                t.goto(int(x - 1) * length, -int(i[0] // x - 1) * length)
            else:
                t.goto(int((i[0] % x) - 1) * length, -int(i[0] // x) * length)
            t.pendown()
            t.setheading(270)
            # 给竖砖勾边
            if valid(i[0], i[-1])[2] == 1:
                for j in range(4):
                    if j % 2 == 0:
                        t.forward(z * length)
                        t.left(90)
                    elif j % 2 == 1:
                        t.forward(w * length)
                        t.left(90)
                t.penup()
            # 给横砖勾边
            else:
                for j in range(4):
                    if j % 2 == 0:
                        t.forward(w * length)
                        t.left(90)
                    elif j % 2 == 1:
                        t.forward(z * length)
                        t.left(90)
                t.penup()

        t.hideturtle()
        scr.exitonclick()


if __name__ == "__main__":
    main()
