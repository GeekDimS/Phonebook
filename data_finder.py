import file_worker as fw

def find(lname, name, phnumber):
    not_eof = True
    res = []
    while not_eof:      # Пока нет конца файла
        not_eof, str_result = fw.read_next()    # Считываем строку из файла
        lname_f, name_f, phnumber_f = str_result.split(',')         # Парсим входную строку
        if lname == lname_f or name == name_f or phnumber == phnumber_f:    # Если есть совпадение хоть по одному полю
            res.append(str_result)      # то добавляем запись в результирующий список
    return res