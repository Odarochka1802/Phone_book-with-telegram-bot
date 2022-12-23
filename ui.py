import cord as s

print('\nВас приветствует телефонная книга')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Поиск по номеру телефона.')
        print('4. Добавить новую запись.')
        print('5. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:

            print(s.retrive())

        elif n == 2:
            search = input('Введите фамилию: ')

            print(s.retrive(surname=search))

        elif n == 3:
            search = input('Введите номер  телефона: ')
            print(s.retrive(number=search))

        elif n == 4:

            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            print(s.create(name, surname, number))

        elif n == 5:
            print('Спасибо за работу!')
            break

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)


