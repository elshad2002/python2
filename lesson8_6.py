from abc import ABC, abstractmethod
import json


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

    @staticmethod
    def json_export():
        ware_dev_for_exp = {}
        ware_list_for_exp = []
        for key in Warehouse.devices_in_warehouse.keys():
            ware_list = []
            for value in Warehouse.devices_in_warehouse[key]:
                if value:
                    ware_list.append(value.get_info())
            if ware_list:
                ware_list.append({'РљРѕР»РёС‡РµСЃС‚РІРѕ':len(ware_list)})
            ware_dev_for_exp = {key: ware_list} if ware_list else None
            if ware_dev_for_exp:
                ware_list_for_exp.append(ware_dev_for_exp)
        ware_dev_for_exp = {'РЈСЃС‚СЂРѕР№СЃС‚РІР° РЅР° СЃРєР»Р°РґРµ': ware_list_for_exp}

        user_dev_for_exp = {}
        user_list_for_exp = []

        for key in Warehouse.user_devices.keys():
            ware_list = []
            for value in Warehouse.user_devices[key]:
                if value:
                    ware_list.append(value.get_info())
            if ware_list:
                ware_list.append({'РљРѕР»РёС‡РµСЃС‚РІРѕ':len(ware_list)})
            user_dev_for_exp = {key: ware_list} if ware_list else None
            if user_dev_for_exp:
                user_list_for_exp.append(user_dev_for_exp)
        user_dev_for_exp = {'РЈСЃС‚СЂРѕР№СЃС‚РІР° Сѓ РїРѕР»СЊР·РѕРІР°С‚РµР»РµР№': user_list_for_exp}
        with open('l8_task6.json', 'w', encoding='utf-8') as out_file:
            json.dump([ware_dev_for_exp, user_dev_for_exp], out_file, indent=4, ensure_ascii=False)

    def __str__(self):
        string_warehouse = '\n'.join(map(str, (sum(self.devices_in_warehouse.values(), []))))
        string_warehouse = 'РЈСЃС‚СЂРѕР№СЃС‚РІР° РЅР° СЃРєР»Р°РґРµ:\n' + string_warehouse if string_warehouse else 'РќР° СЃРєР»Р°РґРµ РЅРµС‚ СѓСЃС‚СЂРѕР№СЃС‚РІ'
        string_user = '\n'.join(map(str, (sum(self.user_devices.values(), []))))
        string_user = 'РЈСЃС‚СЂРѕР№СЃС‚РІР° Сѓ РїРѕР»СЊР·РѕРІР°С‚РµР»РµР№:\n' + string_user if string_user else 'РЈ РїРѕР»СЊР·РѕРІР°С‚РµР»РµР№ СѓСЃС‚СЂРѕР№СЃС‚РІ'
        return string_warehouse + '\n' + string_user


class Device(ABC):
    def __init__(self, brand, serial):
        self._owner = 'Р·Р°РІ.СЃРєР»Р°РґРѕРј'
        if Device.valid_device(brand, serial, self._owner):
            self._brand = brand
            self._serial = serial
            Warehouse.to_warehouse(self)

    def __str__(self):
        return 'РЈСЃС‚СЂРѕР№СЃС‚РІРѕ {}, РЅРѕРјРµСЂ {}, РѕС‚РІРµС‚СЃС‚РІРµРЅРЅС‹Р№ {}.'.format(self._brand, self._serial, self._owner)

    def get_info(self):
        return {'РњРѕРґРµР»СЊ': self._brand, 'РћС‚РІРµС‚СЃС‚РІРµРЅРЅС‹Р№': self._owner, 'РРЅРІРµРЅС‚Р°СЂРЅС‹Р№ РЅРѕРјРµСЂ': self._serial}

    def change_owner(self, owner='Р·Р°РІ.СЃРєР»Р°РґРѕРј'):
        if Device.valid_owner(owner):
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

    @staticmethod
    def valid_owner(owner):
        try:
            with open('l8_task6_workers.txt', encoding='utf-8') as f:
                flag = 0
                for line in f.readlines():
                    if owner in line:
                        flag = 1
                        return True
                if not flag:
                    raise ValueError(f'РћС€РёР±РєР°! РЎРѕС‚СЂСѓРґРЅРёРєР° {owner} РЅРµС‚ РЅР° РїСЂРµРґРїСЂРёСЏС‚РёРё.')
        except ValueError as ex:
            print(ex)
            return False


    @staticmethod
    def valid_device(brand, serial, owner):
        if not Device.valid_owner(owner):
            return False
        try:
            with open('l8_task6_brands.txt', encoding='utf-8') as f:
                flag = 0
                for line in f.readlines():
                    if brand in line:
                        flag = 1
                        break
                if not flag:
                    raise ValueError(f'РћС€РёР±РєР°! РњР°СЂРєРё СѓСЃС‚СЂРѕР№СЃС‚РІР° {brand} РЅРµС‚ РІ РїРµСЂРµС‡РЅРµ.')
            for value in sum(Warehouse.devices_in_warehouse.values(), []):
                if serial == value._serial:
                    raise ValueError(f'РћС€РёР±РєР°! РЈСЃС‚СЂРѕР№СЃС‚РІРѕ СЃ РёРЅРІРµРЅС‚Р°СЂРЅС‹Рј РЅРѕРјРµСЂРѕРј {serial} СѓР¶Рµ РµСЃС‚СЊ РІ Р‘Р”.')
            for value in sum(Warehouse.user_devices.values(), []):
                if serial == value._serial:
                    raise ValueError(f'РћС€РёР±РєР°! РЈСЃС‚СЂРѕР№СЃС‚РІРѕ СЃ РёРЅРІРµРЅС‚Р°СЂРЅС‹Рј РЅРѕРјРµСЂРѕРј {serial} СѓР¶Рµ РµСЃС‚СЊ РІ Р‘Р”.')
        except ValueError as ex:
            print(ex)
            return False
        else:
            return True


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
    printer = Printer('Kyocera', 101)
    scanner = Scanner('РќР ', 102)
    copier = Copier('Xerox', 103)
    Printer('Canon', 104)
    Printer('Printer', 105)
    Printer('Canon', 102)
    print('******************************')
    copier.work()
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
    scanner.change_owner('РљСѓР·РЅРµС† Р’Р°РєСѓР»Р°')
    print('******************************')
    printer.change_owner()
    print('******************************')
    print(Warehouse())
    print('******************************')
    print(Device.how_mush_devices())
    print('******************************')
    print(printer.how_mush_devices())
    Warehouse.json_export()

if __name__ == '__main__':
    main()
