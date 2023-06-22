#  Создать телефонный справочник возможностью добавления записей и чтения.
#  Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий.
#  Также пользователь может добавлять новых людей в справочник в режиме экспорт.



def show_data():
    """эта ф-ция показывает содержимое справочника"""
    with open('data.txt', 'r', encoding ='utf-8') as file:
        book = file.read()#.split('\n')
    return book

def new_data():
    """добавляет строку в справочник"""
    with open('data.txt', 'a', encoding ='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )
    

def find_data():
    """Эта ф-ция ищет информацию в справочнике"""
    with open('data.txt', 'r', encoding ='utf-8') as file:
        book = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in book:
            if temp in i:
                print(i)


while True:
    mode = input('Выберите режим работы справочника' + '\n' +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        break
    else:
        print('No mode')