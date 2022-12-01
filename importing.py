import view

def import_base():
    import1 = view.getNumb('Введите номер --> ')
    import1 += ' '
    import1 += view.getNumb('Введите ФИО --> ')
    import_number(import1)
    view.showinfo('Импорт закончен')

def import_from():
    import_file()
    view.showinfo('Импорт закончен')

def import_number(a):
    f = open('directory', 'a', encoding = 'utf-8')
    f.write(f'\n{a}')
    f.close()

def import_file():
    f1 = open('directory','a')
    f2 = open('file','r')
    f1.write(f"\n{f2.read()}")
    f1.close
    f2.close

def import_substitution():
    view.showinfo('\nНеплохо придумано!!!')