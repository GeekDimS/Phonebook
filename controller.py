from distutils.log import error
import data_finder
import data_provider
import file_worker
import data_former

def run():
    # error = False
    dpf_req = data_provider.dpf1 # Ф-я запроса данных от пользователя Вход: (Void).Выход: (mode,('lastname','name','phone'))
    # mode: 'add'or'search'or'end'or'export html'of'export_json'or'import_html'or'import_json'
    dpf_out = data_provider.dpf2 # Ф-я вывода(печати) найденных данных и сама выводит сообщение меню  Вход: ([('lastname','name','phone'),('lastname2','name2','phone2'),...]) Выход:(Void)
    dfm_list_read = data_former.dfm1 # Ф-я формирования найденных данных от data_finder из вида csv в список кортежей строк для передачи в data_provider Вход:(?список строк в формате csv?) Выход:([('lastname','name','phone'),('lastname2','name2','phone2'),...])
    dfm_list_wriite = data_former.dfm2 # Ф-я формирования строки для записи в файл из ответа от data_provider.dpf1 Вход: ('lastname','name','phone') Выход:(?строка в формате csv?)
    dfn_find = data_finder.find # Ф-я поиска данных в файле Вход: ('lastname','name','phone') Выход: (?список строк в формате csv?)
    fw_read_next = file_worker.fw1 # Ф-я чтения следующей строки данных Вход:(Void) Выход: ('End # достигнут конец файла #', (?строка в формате csv?))
    fw_write = file_worker.add_to_csv_file # Ф-я записи новой строки в конец файла Вход:(?строка в формате csv?) Выход: (Void)

    mode, data = dpf_req()
    if mode == 'end':
        return False
    elif mode == 'add':
        if not fw_write(data):  # Возможны проблемы - нужен список списков
            error('Ошибка добавления записи в файл')
            # Сделать возвращаемое значение из file_worker.add_to_csv_file True, если нет ошибок
    elif mode == 'search':
        # coding here
        data_fainding = dfn_find(data)  # Передаём данные для поиска в базе
        dpf_out(data_fainding)          # Передаём результат для вывода пользователю
        return
    elif mode == 'export_html':
        # coding here
        return
    elif mode == 'export_json':
        # coding here
        return
    elif mode == 'import_html':
        # coding here
        return
    elif mode == 'import_json':
        # coding here
        return
    else:
        error('Ошибка выполнения программы')         # Ф-я обработки ошибок.
        # Написать! Выводит сообщение об ошибке с помощью provider
    