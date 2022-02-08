# Это мой список покупок

shoplist = ['морковь', 'манго', 'яблоки', 'бананы']
print('Я должен сделать', len(shoplist), 'покупки')

print('Покупки:', end=' ')           
for item in shoplist: 
    print(item, end=' ')

print('\nТакже нужно купить риса.')   # \n Вывести на новую строку после итерации
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список теперь выглядит так:', shoplist)

print('Первое что нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)
