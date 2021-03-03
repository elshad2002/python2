from abc import ABC, abstractmethod


class Warehouse:
    devices_in_warehouse = []

    @classmethod
    def to_warehouse(cls, device):
        cls.devices_in_warehouse.append(device)
        print(device, 'РџСЂРёРЅСЏС‚Рѕ РЅР° СЃРєР»Р°Рґ.')

    def __str__(self):
        string = '\n'.join(map(str, self.devices_in_warehouse))
        return 'РЈСЃС‚СЂРѕР№СЃС‚РІР° РЅР° СЃРєР»Р°РґРµ:\n' + string if string else 'РќР° СЃРєР»Р°РґРµ РЅРµС‚ СѓСЃС‚СЂРѕР№СЃС‚РІ'


class Device(ABC):
    def __init__(self, brand, serial, owner='Р·Р°РІ.СЃРєР»Р°РґРѕРј'):
        self._brand = brand
        self._serial = serial
        self.owner = owner

    def __str__(self):
        return 'РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {}, РЅРѕРјРµСЂ {}, РѕС‚РІРµС‚СЃС‚РІРµРЅРЅС‹Р№ {}.'.format(self._brand, self._serial, self.owner)

    @abstractmethod
    def work(self):
        pass


class Printer(Device):
    def work(self):
        print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {} РїРµС‡Р°С‚Р°РµС‚.'.format(self._brand))


class Scanner(Device):
    def work(self):
        print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {} СЃРєР°РЅСЂСѓРµС‚.'.format(self._brand))


class Copier(Device):
    def work(self):
        print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {} РєРѕРїРёСЂСѓРµС‚.'.format(self._brand))


def main():
    printer = Printer('Ricoh', 101)
    scanner = Scanner('HP', 102)
    copier = Copier('Xerox', 103)
    print(printer)
    printer.work()
    scanner.work()
    copier.work()
    print(Warehouse())
    Warehouse.to_warehouse(printer)
    Warehouse.to_warehouse(scanner)
    Warehouse.to_warehouse(copier)
    print(Warehouse())


if __name__ == '__main__':
    main()
