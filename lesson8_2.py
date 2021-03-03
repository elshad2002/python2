class UserDivZeroError(Exception):
    def __init__(self, message):
        self.message = message


def main():
    while True:
        dividend = input('Р’РІРµРґРёС‚Рµ РґРµР»РёРјРѕРµ РёР»Рё "q" РґР»СЏ РІС‹С…РѕРґР°: ')
        if dividend == 'q': break
        divisor = input('Р’РІРµРґРёС‚Рµ РґРµР»РёС‚РµР»СЊ РёР»Рё "q" РґР»СЏ РІС‹С…РѕРґР°: ')
        if divisor == 'q': break
        try:
            if float(divisor) == 0:
                raise UserDivZeroError('РќР° РЅРѕР»СЊ РґРµР»РёС‚СЊ РЅРµР»СЊР·СЏ!!!!!!11')
            else:
                print(f'Р§Р°СЃС‚РЅРѕРµ: {float(dividend)/float(divisor):.2f}')
        except UserDivZeroError as ex:
            print(ex)
        except ValueError as ex:
            print(ex)

if __name__ == '__main__':
    main()