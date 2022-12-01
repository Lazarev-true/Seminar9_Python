import exporting as ex
import importing as im
import database as db
    
com = '1 - импорт вручную\n\
2 - импорт из файла\n\
3 - импортозамещение\n\
4 - экспорт\n\
5 - поиск контакта'

commands = {'1': im.import_base, 
            '2': im.import_from,
            '3': im.import_substitution, 
            '4': ex.unload, 
            '5': db.search}