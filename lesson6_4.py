class Car:
    '''РђРІС‚РѕРјРѕР±РёР»СЊ'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'РќРѕРІР°СЏ РјР°С€РёРЅР°: {self.name} (С†РІРµС‚ {self.color}), РјР°С€РёРЅР° РїРѕР»РёС†РµР№СЃРєР°СЏ - {self.is_police}')

    def go(self):
        print(f'{self.name}: РњР°С€РёРЅР° РїРѕРµС…Р°Р»Р°.')

    def stop(self):
        print(f'{self.name}: РњР°С€РёРЅР° РѕСЃС‚Р°РЅРѕРІРёР»Р°СЃСЊ.')

    def turn(self, direction):
        print(f'{self.name}: РњР°С€РёРЅР° РїРѕРІРµСЂРЅСѓР»Р°: {"РЅР°Р»РµРІРѕ" if direction == 0 else "РЅР°РїСЂР°РІРѕ"}.')

    def show_speed(self):
        return f'{self.name}: РЎРєРѕСЂРѕСЃС‚СЊ Р°РІС‚РѕРјРѕР±РёР»СЏ: {self.speed}.'


class TownCar(Car):
    '''Р“РѕСЂРѕРґСЃРєРѕР№ Р°РІС‚РѕРјРѕР±РёР»СЊ'''

    def show_speed(self):
        return f'{self.name}: РЎРєРѕСЂРѕСЃС‚СЊ Р°РІС‚РѕРјРѕР±РёР»СЏ: {self.speed}. РџСЂРµРІС‹С€РµРЅРёРµ СЃРєРѕСЂРѕСЃС‚Рё!' \
            if self.speed > 60 else f"{self.name}: РЎРєРѕСЂРѕСЃС‚СЊ Р°РІС‚РѕРјРѕР±РёР»СЏ: {self.speed}."


class WorkCar(Car):
    '''Р“СЂСѓР·РѕРІРѕР№ Р°РІС‚РѕРјРѕР±РёР»СЊ'''

    def show_speed(self):
        return f'{self.name}: РЎРєРѕСЂРѕСЃС‚СЊ Р°РІС‚РѕРјРѕР±РёР»СЏ: {self.speed}. РџСЂРµРІС‹С€РµРЅРёРµ СЃРєРѕСЂРѕСЃС‚Рё!' \
            if self.speed > 40 else f"{self.name}: РЎРєРѕСЂРѕСЃС‚СЊ Р°РІС‚РѕРјРѕР±РёР»СЏ: {self.speed}."


class SportCar(Car):
    '''РЎРїРѕСЂС‚РёРІРЅС‹Р№ Р°РІС‚РѕРјРѕР±РёР»СЊ'''


class PoliceCar(Car):
    '''РџРѕР»РёС†РµР№СЃРєРёР№ Р°РІС‚РѕРјРѕР±РёР»СЊ'''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar("Audi", "Р±РµР»С‹Р№", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Р“СЂСѓР·РѕРІРёС‡РѕРє"', 'С…Р°РєРё', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('"РЎРїРѕСЂС‚РёРІРєР°"', 'РєСЂР°СЃРЅС‹Р№', 120)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"РњР°Р»СЋС‚РєР°"', 'Р¶С‘Р»С‚С‹Р№', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nРњР°С€РёРЅР° {town_car.name} (С†РІРµС‚ {town_car.color})')
print(f'РњР°С€РёРЅР° {police_car.name} (С†РІРµС‚ {police_car.color})')
