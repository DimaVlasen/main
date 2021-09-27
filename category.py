
print('Привет, давай определим категорию :)')
count = 0

while True:
    category = int (input('Введи число от 1 до 25='))
    if category < 10:
     print('Вы имеете низкую категорию')
    elif 11 <= category <= 15:
     print('Вы имеете среднюю категорию')
    else:
     print('Вы имеете высокую категорию')
    break
print('Пока!')
