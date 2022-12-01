import view
import loading

f = open('directory', 'r', encoding = 'utf-8')
lst = f.read().split('\n')

number = {}

for i in lst:
    key = i.split(' ')[0]
    value = ' '.join(i.split()[1:])
    number[key] = value

f.close()

def search():
    view.showinfo('1 - по номеру или 2 - по ФИО')
    searchIn = view.getNumb('Искать --> ')
    if searchIn == '1':
        number_data()
    elif searchIn == '2':
        FCs_data()
    else:
        view.showinfo('Такого варианта нет')

def number_data():
    while True:
        search1 = view.getNumb('Введите номер --> ')
        view.showinfo('')
        loading.progress()
        if search1 not in number:
            view.showinfo('Такого номера нет')
            continue
        else:
            result = number[search1]
            break
    view.showinfo(result)

def FCs_data():
    while True:
        search2 = view.getNumb('Введите ФИО --> ')
        view.showinfo('')
        loading.progress()
        if search2 not in number.values():
            view.showinfo('Такого ФИО нет')
            continue
        else:
            result = list(number.keys())[list(number.values()).index(search2)]
            break
    view.showinfo(result)