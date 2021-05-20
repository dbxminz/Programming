from reports.myturtle import *
import turtle

# 케이크 1단
h = 60

w = 420
x, y = -210, -150

draw_rectangle(w, h, x, y, f_color='lightgreen')
for i in range(w // 30):
    radius = 15
    if i % 2 == 0:
        draw_squarepolygon(x+15, y+30, radius, side=4, f_color="red")
    else:
        draw_squarepolygon(x+15, y+30, radius, side=4, f_color="royalblue")
    x += 30

# 케이크 2단
w = 330
x, y = -165, -90

draw_rectangle(w, h, x, y, f_color='khaki')
for i in range(w//30):
    radius = 15
    if i % 2 == 0:
        draw_squarepolygon(x+15, y+60-1.809*radius, radius, side=5, f_color="forestgreen")
    else:
        draw_squarepolygon(x+15, y+60-1.809*radius, radius, side=5, f_color="goldenrod")
    x += 30

# 케이크 3단
w = 270
x, y = -135, -30

draw_rectangle(w, h, x, y, f_color='peachpuff')
for i in range(w//30):
    radius = 15
    if i % 2 == 0:
        draw_squarepolygon(x+15, y+30, radius, side=None, f_color="chocolate")
    else:
        draw_squarepolygon(x+15, y+30, radius, side=None, f_color="royalblue")
    x += 30

# 별 그리기
draw_line(0, 30, 100, direction=90, p_size=5)
draw_star(-20, 145, 40, p_color="royalblue", f_color="royalblue")

# 촛불 그리기
y = 30

for x in [-125, -65, 55, 115]:
    draw_candle(10, 20, x, y, 8)

turtle.done()




