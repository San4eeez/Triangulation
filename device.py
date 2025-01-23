import math

class Device:
    def __init__(self, x, y):
        self.x = x  # Координата x устройства
        self.y = y  # Координата y устройства

    def is_clicked(self, x, y):
        # Проверка, было ли устройство нажато
        return math.sqrt((x - self.x)**2 + (y - self.y)**2) <= 5

    def is_inside_all_towers(self, towers):
        # Проверка, находится ли устройство внутри всех башен
        return all(math.sqrt((self.x - tower.x) ** 2 + (self.y - tower.y) ** 2) <= tower.r for tower in towers)
