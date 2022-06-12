import data_finder
import data_provider
import file_worker
import data_former

def run():
    # error = False
    data_provider.dpf1 = dpf_req # Ф-я запроса данных от пользователя Вход: (Void).Выход: ('add'or'search',('lastname','name','phone')) 
    data_provider.dpf2 = dpf_out # Ф-я вывода(печати) найденных данных и сама выводит сообщение Вход: ([('lastname','name','phone'),('lastname2','name2','phone2'),...]) Выход:(Void)

    data_former.dfm1 = dfm_list_read # Ф-я формирования найденных данных от data_finder из вида csv в список кортежей строк для передачи в data_provider Вход:(?список строк в формате csv?) Выход:([('lastname','name','phone'),('lastname2','name2','phone2'),...])
    data_former.dfm2 = dfm_list_wriite # Ф-я формирования строки для записи в файл из ответа от data_provider.dpf1 Вход: ('lastname','name','phone') Выход:(?строка в формате csv?)

    data_finder.dfn1 = dfn_find # Ф-я поиска данных в файле Вход: ('lastname','name','phone') Выход: (?список строк в формате csv?)

    file_worker.fw1 = fw_read_next # Ф-я чтения следующей строки данных Вход:(Void) Выход: ('End # достигнут конец файла #', (?строка в формате csv?))
    file_worker.fw2 = fw_write # Ф-я записи новой строки в конец файла Вход:(?строка в формате csv?) Выход: (Void)