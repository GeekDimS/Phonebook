#'csv', html. json
import csv
import json

def find_csv_separator(file_name):
    sniffer = csv.Sniffer()
    with open(file_name, encoding = 'UTF-8') as file:
        separator = sniffer.sniff(file.read(1000)).delimiter
    return separator

file_name_csv = "database.csv"
file_name_import_csv = "data.csv"
file_name_html = "data.html"
file_name_json = "data.json"

def read_from_csv_file( file_name = file_name_csv):
    '''
    Функция чтения из csv файла (на выходе список словарей)
    '''
    data = []  
    with open(file_name, 'r', encoding = 'UTF-8') as file_csv:
        reader_from_file = csv.DictReader(file_csv)
        for row in reader_from_file:
            data.append(row)
    return data


def write_to_csv_file(data, file_name = file_name_csv):
    '''
    Функция записи в csv файл (вход -> список списков данных)
    например, data = [["Ледов", "Иван", "+72222222222"],
                      ["Горшкова", "Инна", "+77777777777"]]
    '''
    with open(file_name, 'w', encoding = 'UTF-8') as file_csv:
        writer_to_file = csv.writer(file_csv)
        for row in data:
            writer_to_file.writerow(row)


def add_to_csv_file(data: list, file_name = file_name_csv):
    '''
    Функция добавления данных (вход -> список списков данных) в csv файл
    например, data = [["Ледов", "Иван", "+72222222222"]]
    '''
    with open(file_name, 'a', encoding = 'UTF-8') as file_csv:
        writer_to_file = csv.writer(file_csv)
        for row in data:
            writer_to_file.writerow(row)


def export_from_csv_to_json_file(file_name_from = file_name_csv, file_name_to = file_name_json):
    '''
    Функция экспорта из csv файла в json файл 
    '''
    data = read_from_csv_file(file_name_from)
    with open(file_name_to, 'w', encoding = 'UTF-8') as file_json:
        json.dump(data, file_json)


def read_from_json_file(file_name = file_name_json):
    '''
    Функция чтения из json файла (на выходе список словарей)
    '''
    data = read_from_csv_file(file_name)
    with open(file_name_json, 'r', encoding = 'UTF-8') as file_json:
        data = json.load(file_json)
    return data  

def import_from_json_to_csv_file(file_name_from = file_name_json, file_name_to = file_name_import_csv):
    '''
    Функция импорта из json в csv файл 
    '''


def export_from_csv_to_html_file(file_name_from = file_name_csv, file_name_to = file_name_html):
    '''
    Функция экспорта из csv файла в html файл 
    '''
    data = read_from_csv_file(file_name_from)

    style = 'style="font-size:18px"'
    data_html = '<html>\n <head></head>\n <body>\n'
    for item in data:
        # data_html += '<p {}>Lastname: {} </p>'.format(style, item['Lastname'])
        # data_html += '<p {}>Name: {} </p>'.format(style, item['Name'])
        # data_html += '<p {}>Phone: {} </p>\n'.format(style, item['Phone'])
        data_html += '<p {}>Lastname: {}, Name: {}, Phone: {}\n</p>'\
            .format(style, item['Lastname'],  item['Name'], item['Phone'])
    data_html += '<body>\n</html>'    

    with open(file_name_to, 'w', encoding = 'UTF-8') as file_html:
        file_html.write(data_html)
    
def import_from_html_to_csv_file(file_name_from = file_name_html, file_name_to = file_name_import_csv):
    '''
    Функция импорта из html в csv файл 
    '''

  

# initial_data =[["Lastname", "Name", "Phone"], 
#             ["Петров", "Илья", "+79234567898"], 
#             ["Бобров", "Петр", "+79274567898"], 
#             ["Бочкова", "Анна", "+79784336598"],
#             ["Горшкова", "Инна", "+77777777777"],
#             ["Печкин", "Иван", "+74951234567"],
#             ["Белов", "Иван", "+73333333333"],
#             ["Белоусова", "Инна", "+73333333367"],
#             ["Мор", "Илья", "+74956767677"]]

# write_to_csv_file(initial_data)
# data = read_from_csv_file()
# print(data)

# add_data = [["Ледов", "Иван", "+72222222222"]]
# add_to_csv_file(add_data)
# data = read_from_csv_file()
# print(data)

# export_from_csv_to_json_file()
# data = read_from_json_file()
# print(f'json - {data}')

# export_from_csv_to_html_file()

# find_item = "Бобров"
# for item in data:
#     if find_item in item.values():
#         print(item)
