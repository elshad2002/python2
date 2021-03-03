from abc import ABC, abstractmethod


class Warehouse:

    devices_in_warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}
    user_devices = {'Printer': [], 'Scanner': [], 'Copier': []}

    @classmethod
    def to_warehouse(cls, *devices, from_user=False):
        if not from_user:
            for device in devices:
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, 'РџСЂРёРЅСЏС‚Рѕ РЅР° СЃРєР»Р°Рґ.')
        else:
            for device in devices:
                cls.user_devices[str(device.__class__.__name__)].remove(device)
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, 'РџСЂРёРЅСЏС‚Рѕ РЅР° СЃРєР»Р°Рґ.')

    @classmethod
    def from_warehouse(cls, device):
        cls.devices_in_warehouse[str(device.__class__.__name__)].remove(device)
        cls.user_devices[str(device.__class__.__name__)].append(device)
        print(device, 'РџРµСЂРµРґР°РЅРѕ СЃРѕ СЃРєР»Р°РґР°.')

    def __str__(self):
        string_warehouse = '\n'.join(map(str, (sum(self.devices_in_warehouse.values(), []))))
        string_warehouse = 'РЈСЃС‚СЂРѕР№СЃС‚РІР° РЅР° СЃРєР»Р°РґРµ:\n' + string_warehouse if string_warehouse else 'РќР° СЃРєР»Р°РґРµ РЅРµС‚ СѓСЃС‚СЂРѕР№СЃС‚РІ'
        string_user = '\n'.join(map(str, (sum(self.user_devices.values(), []))))
        string_user = 'РЈСЃС‚СЂРѕР№СЃС‚РІР° Сѓ РїРѕР»СЊР·РѕРІР°С‚РµР»РµР№:\n' + string_user if string_user else 'РЈ РїРѕР»СЊР·РѕРІР°С‚РµР»РµР№ СѓСЃС‚СЂРѕР№СЃС‚РІ'
        return string_warehouse + '\n' + string_user


class Device(ABC):
    def __init__(self, brand, serial, owner='Р·Р°РІ.СЃРєР»Р°РґРѕРј'):
        self._brand = brand
        self._serial = serial
        self._owner = owner

    def __str__(self):
        return 'РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {}, РЅРѕРјРµСЂ {}, РѕС‚РІРµС‚СЃС‚РІРµРЅРЅС‹Р№ {}.'.format(self._brand, self._serial, self._owner)

    def change_owner(self, owner='Р·Р°РІ.СЃРєР»Р°РґРѕРј'):
        print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {} РїРµСЂРµРїРёСЃР°РЅРѕ СЃ {} РЅР° {}.'.format(self._brand, self._owner, owner))
        self._owner = owner
        if self._owner == 'Р·Р°РІ.СЃРєР»Р°РґРѕРј':
            Warehouse.to_warehouse(self, from_user=True)
        else:
            Warehouse.from_warehouse(self)

    @classmethod
    def how_mush_devices(cls, device='All'):
        if str(device) == 'All':
            string_warehouse = {key: len(value) for key, value in Warehouse.devices_in_warehouse.items()}
            string_user = {key: len(value) for key, value in Warehouse.user_devices.items()}
        else:
            string_warehouse = {device: len(Warehouse.devices_in_warehouse[device])}
            string_user = {device: len(Warehouse.user_devices[device])}
        string_warehouse = 'РЈСЃС‚СЂРѕР№СЃС‚РІР° РЅР° СЃРєР»Р°РґРµ:\n' + '\n'.join('{}: {}'.format(key, value) for key, value in string_warehouse.items()) + '\nРС‚РѕРіРѕ: ' + str(sum(string_warehouse.values()))
        string_user = 'РЈСЃС‚СЂРѕР№СЃС‚РІР° Сѓ РїРѕР»СЊР·РѕРІР°С‚РµР»РµР№:\n' + '\n'.join('{}: {}'.format(key, value) for key, value in string_user.items()) + '\nРС‚РѕРіРѕ: ' + str(sum(string_user.values()))
        return string_warehouse + '\n' + string_user

    @abstractmethod
    def work(self):
        print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {}, РЅРѕРјРµСЂ {} РЅР°С…РѕРґРёС‚СЃСЏ РЅР° СЃРєР»Р°РґРµ.'.format(self._brand, self._serial))


class Printer(Device):
    def work(self):
        if self._owner == 'Р·Р°РІ.СЃРєР»Р°РґРѕРј':
            super().work()
        else:
            print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ РїРµС‡Р°С‚Р°РµС‚.')

    @classmethod
    def how_mush_devices(cls, device='Printer'):
        return super().how_mush_devices(device)


class Scanner(Device):
    def work(self):
        if self._owner == 'Р·Р°РІ.СЃРєР»Р°РґРѕРј':
            super().work()
        else:
            print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ СЃРєР°РЅСЂСѓРµС‚.')

    @classmethod
    def how_mush_devices(cls, device='Scanner'):
        return super().how_mush_devices(device)


class Copier(Device):
    def work(self):
        if self._owner == 'Р·Р°РІ.СЃРєР»Р°РґРѕРј':
            super().work()
        else:
            print('РЈСЃС‚СЂРѕР№СЃС‚РІРѕ РєРѕРїРёСЂСѓРµС‚.')

    @classmethod
    def how_mush_devices(cls, device='Copier'):
        return super().how_mush_devices(device)


def main():
    print(Warehouse())
    printer = Printer('Ricoh', 101)
    scanner = Scanner('HP', 102)
    copier = Copier('Xerox', 103)
    printer_2 = Printer('Canon', 104)
    print('******************************')
    copier.work()
    print('******************************')
    Warehouse.to_warehouse(printer, scanner, copier, printer_2)
    print('******************************')
    print(Warehouse())
    print('******************************')
    printer.change_owner('Р’Р°Р»РµРЅС‚РёРЅ Р’Р°Р»РµРЅС‚РёРЅРѕРІ')
    print('******************************')
    print(Warehouse())
    print('******************************')
    copier.change_owner('Р›СЋРґРІРёРі Р’Р°РЅС‹С‡')
    print('******************************')
    copier.work()
    print('******************************')
    printer.change_owner()
    print('******************************')
    print(Warehouse())
    print('******************************')
    print(Device.how_mush_devices())
    print('******************************')
    print(printer.how_mush_devices())


if __name__ == '__main__':
    main()