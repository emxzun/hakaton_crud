import json
from time import strftime
from settings import db
from json.decoder import JSONDecodeError
from datetime import datetime
from pprint import pprint


# list_ = [
#     {
#         'id': 1,
#         'price': 243243,
#         'title': 'название',
#         'description': 'описание',
#         'created_at': '24.08.22 19:01'
#     }
# ]


def get_all_data():
    with open(db) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []



def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите название: '),
        'price': input('Введите цену: '),
        'description': input('Введите описание: '),
        'created_at': datetime.now().strftime('%d.%m.%Y %H:%M'),
        'status': 'Продается'.lower()
    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(db, 'w') as f:
        json.dump(json_data, f, indent=4)




def get_data_by_id():
    id_ = input('Введите Id: ')
    for obj in get_all_data():
        if obj['id'] == id_:
            print(obj)
    return 'Not found'


def delete_data():
    pprint(get_all_data())
    id_ = input('Введите Id: ')
    data = get_all_data()
    for x in data:
        if x['id'] == id_:
            data.remove(x)
            break
    with open(db, 'w') as f:
        json.dump(data, f, indent=4)


def update():
    id_ = input('Введите Id: ')
    data = get_all_data()
    for x in data:
        if x['id'] == id_:
            x['title'] = input('Введите название: ') or x['title']
            x['price'] = int(input('Введите цену: ')) or x['price']
            x['description'] = input('Введите описание: ') or x['description']
            x['status'] = input('Введите статус(продано/продается): ') or x['status']
            x['updated_at'] = datetime.now().strftime('%d%m%y, %H:%M')
            break
    with open(db, 'w') as f:
        json.dump(data, f, indent=4)

data = get_all_data() 
def filter_():
    global data
    for x in data:
        if x['status'] == 'продается':
            with open(db) as f:
                pprint(get_all_data())
        elif x['status'] == 'продано':
            pprint(get_all_data())
        elif x['price'] > 200:
            pprint(get_all_data())
        else:
            None
       
res = list(filter(filter_(), data))



def info():
    print('-' * 50)
    print(' ')
    print('''
    Введите операцию которую хотите совершить:
    1)create - создать новый продукт
    2)delete - удалить продукт
    3)list - список всех продуктов
    4)retrieve - получить продукт по id
    5)update - изменить данные
    ''')
    inp = input()
    
    if inp == 'create':
        create_data()
    elif inp == 'delete':
        delete_data()
    elif inp == 'list':
        pprint(get_all_data())
    elif inp == 'update':
        update()
    elif inp == 'retrieve':
        get_data_by_id()
    elif inp == 'list':
        print(res)
    
    


    inp2 = input('Хотите продолжить?(yes/no): ').lower()
    if inp2 == 'yes':
        info()
    else:
        None

        
