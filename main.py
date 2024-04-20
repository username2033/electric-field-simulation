import tkinter as tk
from tkinter import Canvas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Запросить пользователя ввести количество зарядов
n = int(input("Введите количество зарядов: "))

# Инициализация списка для хранения значений зарядов и их координат
charges = []
max_x=0
max_y=0
min_x=0
min_y=0
for _ in range(n):
    q = float(input(f"Введите величину заряда {len(charges) + 1}: "))
    x = float(input(f"Введите координату x для заряда {len(charges) + 1}: "))
    y = float(input(f"Введите координату y для заряда {len(charges) + 1}: "))
    if x>max_x:
        max_x=x
    elif x<min_x:
        min_x=x
    if y>max_y:
        max_y=y
    elif y<min_y:
        min_y=y
    charges.append((q, x, y))

# Создание сетки для визуализации поля
x = np.linspace(min_x-4, 2*max_x+3, 1000)
y = np.linspace(min_y-4, 2*max_y+3, 1000)
X, Y = np.meshgrid(x, y)

# Расчет электрического поля для каждой точки сетки
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
k = 8.987551787e9 # Постоянная Кулона
for charge in charges:
    q, cx, cy = charge
    r = np.sqrt((X - cx)**2 + (Y - cy)**2)
    Ex += k * (q * (X - cx)) / r**3
    Ey += k * (q * (Y - cy)) / r**3

# Вывод визуализации электрического поля
fig, ax = plt.subplots()
ax.streamplot(X, Y, Ex, Ey, density=2, arrowsize=2)
for charge in charges:
    q, cx, cy = charge
    color = 'red' if q > 0 else 'blue'  # Определение цвета в зависимости от заряда
    ax.scatter(cx, cy, c=color, s=100, edgecolors='k', zorder=5)  # Отображение зарядов
root = tk.Tk()
root.title("Электрическое поле, создаваемое точечными зарядами")
plt.title('Электрическое поле, создаваемое точечными зарядами')
plt.xlabel('x')
plt.ylabel('y')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Запуск приложения tkinter
tk.mainloop()
