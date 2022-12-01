import view
import database as db

def unload():
    while True:
            FCs = view.getNumb('Искать контакт по ФИО --> ')
            if FCs == '*':
                break
            elif FCs not in db.number.values():
                view.showinfo('Такого ФИО нет')
                continue
            else:
                contact = list(db.number.keys())[list(db.number.values()).index(FCs)]
                contact += ' ' + FCs
                export_file(contact)
                view.showinfo('Экспорт закончен для закрытия введите *')
    
def export_file(a):
    f = open('export', 'a', encoding = 'utf-8')
    f.write(f'{a}\n')
    f.close()