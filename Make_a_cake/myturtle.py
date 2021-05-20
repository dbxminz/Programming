import turtle

def draw_line(x, y, length, direction=0, p_size=1):
    """
    x, y : 직선의 출발점 좌표
    length : 선의 길이
    direction : 방향(0-동, 90-북, 180-서, 270-남)
    p_size : 직선의 굵기 (픽셀)
    """
    pen = turtle.Turtle()
    pen.pensize(p_size)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(direction)
    pen.forward(length)

    pen.hideturtle()


def draw_rectangle(w, h, x, y, p_size=1, p_color="black", f_color=None):
    """
    w,h : 사각형의 가로, 세로 (int)
    x, y : 사각형의 기준점(좌측 하단점) (int)
    p_size : 선의 굵기
    p_color : 선의 색깔
    f_color : 채우기 색깔
    """
    pen = turtle.Turtle()
    pen.color(p_color)
    pen.pensize(p_size)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if f_color:
        pen.fillcolor(f_color)
        pen.begin_fill()
        for side in [w, h]*2:   # [w, h, w, h]
            pen.forward(side)
            pen.left(90)
        pen.end_fill()
    else:
        for side in [w, h]*2:   # [w, h, w, h]
            pen.forward(side)
            pen.left(90)

    pen.hideturtle()


def draw_squarepolygon(x, y, radius, side=None, p_color="black", f_color=None):
    """
    x, y : 기준점 좌표
    radius : 외접원의 반지름
    side : 변의 수
    p_color, f_color : 테두리 및 채우기 색
    """
    pen = turtle.Turtle()
    pen.color(p_color)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if f_color:
        pen.fillcolor(f_color)
        pen.begin_fill()
        pen.circle(radius, steps=side)
        pen.end_fill()
    else:
        pen.circle(radius, steps=side)

    pen.hideturtle()


def draw_star(x, y, length, p_color="black", f_color=None):
    """
    x, y : 별의 시작점 좌표
    length : 별의 길이
    p_color, f_color : 선 및 채우기 색
    """
    pen = turtle.Turtle()
    pen.color(p_color)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if f_color:
        pen.fillcolor(f_color)
        pen.begin_fill()
        for n in range(5):
            pen.forward(length)
            pen.right(144)
        pen.end_fill()
    else:
        for n in range(5):
            pen.forward(length)
            pen.right(144)
    pen.hideturtle()

def draw_candle(w, h, x, y, f_radius):
    """
    w, h :촛불의 폭과 넓이
    x, y : 촛불의 기준점(좌측 하단점 좌표)
    f_radius : 촛불의 반경 (촛불 심지의 길이로도 사용)
    """
    pen = turtle.Turtle()
    pen.penup()

    pen.goto(x, y)
    pen.pendown()

    for side in [w, h] * 2:  # [w, h, w, h]
        pen.forward(side)
        pen.left(90)

    x += 5
    y += 20

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.pencolor("red")
    pen.fillcolor("red")

    pen.begin_fill()
    pen.circle(f_radius)
    pen.end_fill()

    pen.pencolor("black")

    pen.hideturtle()

    draw_line(x, y, f_radius // 2, direction=90, p_size=3)




