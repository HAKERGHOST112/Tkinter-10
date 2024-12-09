from tkinter import *

# Координаты
coordinates_x = None
coordinates_y = None
moving = False  # БЕЗ ДВИЖЕНИЙ

def set_coordinates(event):
#Обновление координат при нажатии ЛКМ
    global coordinates_x, coordinates_y, moving
    coordinates_x, coordinates_y = event.x, event.y  # сохраняет координаты клика (event.x и event.y
    if not moving:
        moving = True
        motion()

def motion():
    #перемещения к точке нажатия
    global coordinates_x, coordinates_y, moving

    if coordinates_x is None or coordinates_y is None:
        return

    # Начальные координаты
    x1, y1, x2, y2 = c.coords(ball)
    center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2  # Центр круга


    dx = coordinates_x - center_x
    dy = coordinates_y - center_y


    scorost = 2  # Скорость движения
    distance = (dx**2 + dy**2)**0.5  # Расстояние до клика

    if distance > 1:  # Если расстояние больше 1 пикселя
        dx, dy = dx / distance * scorost, dy / distance * scorost
        c.move(ball, dx, dy)
        root.after(10, motion)  # Идёт дальше движение
    else:
        moving = False  # Остановки при достижении цели


root = Tk()
root.title("Клик в точку")
c = Canvas(root, width=300, height=300, bg='white')
c.pack()


ball = c.create_oval(140, 140, 160, 160, fill='green')

# ЛКМ
c.bind('<Button-1>', set_coordinates)

root.mainloop()
