# File name if.py

number = 26
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздравляю, вы унадали, ') # Начало нового блока
    print('(хотя и не выиграли никакого приза!)') # Конец нового блока
elif guess < number:
    print('Нет, загаданое число немного больше этого.') # Ещё один блок 
    # Внутри блока вы можете выполнять всё что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.') 
    # Чтобы попасть сюда, guees должно быть больше, чем number
print('Завершено')
# Это последнее выражение выполняется всегда после выполнения оператора if
