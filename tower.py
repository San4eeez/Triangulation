import math
import tkinter as tk

class Tower:
    def __init__(self, x, y, r):
        self.x = x  # Координата x башни
        self.y = y  # Координата y башни
        self.r = r  # Радиус башни
        self.x_entry = None  # Поле ввода для координаты x
        self.y_entry = None  # Поле ввода для координаты y
        self.r_entry = None  # Поле ввода для радиуса

    def is_clicked(self, x, y):
        # Проверка, была ли башня нажата
        return math.sqrt((x - self.x)**2 + (y - self.y)**2) <= self.r

    def create_entries(self, root, row):
        # Создание полей ввода для параметров башни
        self.x_entry = tk.Entry(root, width=5)
        self.x_entry.insert(0, str(self.x))
        self.x_entry.grid(row=row, column=1)

        self.y_entry = tk.Entry(root, width=5)
        self.y_entry.insert(0, str(self.y))
        self.y_entry.grid(row=row, column=2)

        self.r_entry = tk.Entry(root, width=5)
        self.r_entry.insert(0, str(self.r))
        self.r_entry.grid(row=row, column=3)

    def update_params(self):
        # Обновление параметров башни из полей ввода
        self.x = float(self.x_entry.get())
        self.y = float(self.y_entry.get())
        self.r = float(self.r_entry.get())
