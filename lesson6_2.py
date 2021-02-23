class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return f"{self._length} Рј * {self._width} Рј * 25 РєРі * 5 СЃРј = {(self._length * self._width * 25 * 5) / 1000} С‚"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())