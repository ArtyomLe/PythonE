#using_dict.py

# 'ab' - address book
ab = { 'Artyom'   : 'artyom@gmail.com',
       'Larry'    : 'larry@wall.org',
       'Matsumoto': 'matz@ruby-lang.org',
       'Spammer'  : 'spammer@hotmail.com'
     }

print("Адрес Artyom'a:", ab['Artyom'])

# Удаление пары ключей
del ab['Spammer']
print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])
