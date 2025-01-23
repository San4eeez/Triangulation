import tkinter as tk
from triangulation_app import TriangulationApp

if __name__ == "__main__":
    root = tk.Tk()  # Создаем главное окно
    app = TriangulationApp(root)  # Инициализируем приложение
    root.mainloop()  # Запускаем главный цикл обработки событий
