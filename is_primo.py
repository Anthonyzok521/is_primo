''''Script'''
import math
from colorama import Back, Fore, Style, init

init(True)

def is_primo(n: int) -> (str, bool): # type: ignore
    '''Return a Boolean if is primo
        Args:
            n(int)
        Return:
            Boolean
        '''

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return (Back.RED, False)

    return (Back.GREEN, True)

def padding(digit: int, zero: str = '') -> (str, str, int): # type: ignore
    '''Padding'''
    pd_l = '   ' + zero
    pd_r = '  '
    p = 1

    if digit >= 3:
        p = (digit - 2) + 1
        pd_l = str(' ' * (p + 1)) + zero
        pd_r = str(' ' * (p + 1) )

    return (pd_l, pd_r, p)

def list_num_primos(number: int):
    '''Show a list of numbers primo'''
    count = 0
    row = 1
    a_row = row

    digits = int( math.log10(number) ) + 1

    pd_l, pd_r, p = padding(digits, '0')

    end = Back.WHITE+''
    style = Style.BRIGHT + Fore.WHITE
    bg = Back.GREEN

    n_primos = []

    print()

    for i in range(2, number + 1):
        if count > 7:
            end = '\n'
            row += 1
            count = -1

        if i > 9:
            pd_l = str('  ')
            pd_r = str(' ' * (p + 2))
        if i > 99:
            pd_l = str('  ')
            pd_r = str(' ' * (p + 1))
        if i > 999:
            pd_l = '  '
            pd_r = str(' ' * p)

        if i in (2, 3, 5, 7):
            bg = Back.GREEN
            print(style + bg + pd_l +str(i)+pd_r, Back.WHITE + str(' '*3), sep='', end=end)
            n_primos.append(i)

        else:
            bg, primo = is_primo(i)
            print(style + bg + pd_l +str(i)+pd_r, Back.WHITE + str(' '*3), sep='', end=end)
            if primo:
                n_primos.append(i)
        count += 1

        if row > a_row:
            a_row = row
            end = Back.WHITE+''

    pd_l, pd_r, p = padding(digits)

    if 10 - count != 10:
        for i in range(count + 1, 10):
            print(style + Back.GREEN + pd_l+'  '+pd_r, Back.WHITE + str(' '*3), sep='', end=end)

    #print(count, 10 - count)
    print(f'''
Number: {number} is {'' if number in n_primos else 'not '}primo''')

if __name__ == '__main__':
    try:

        num = int(input("Enter a number: "))
        list_num_primos(num)
    except TypeError:
        print('Just numbers integers')
