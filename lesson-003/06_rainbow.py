# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)



# step = 5
# x, y = 50, 50
# for color in rainbow_colors:
#     start_point = sd.get_point(x, y)
#     end_point = sd.get_point(x + 300, y + 400)
#     sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
#     x += step
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(850, -200)
radius = 700
i = 0
for color in rainbow_colors:
    sd.circle(center_position=point, radius=radius, color=color, width=4)
    i += 1
    radius += 5


sd.pause()