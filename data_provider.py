import data_checker
import data_finder
import file_worker
import data_former
import tkinter
from tkinter import *
from tkinter import messagebox

# mode = ""
# data = [[]]

ADD_WINDOW_HEADER = "Добавление в базу"
FIND_WINDOW_HEADER = "Поиск в базе"

def export_to_json():
    file_worker.export_from_csv_to_json_file()
    # global mode
    # mode = "export_json"


def export_to_html():
    file_worker.export_from_csv_to_html_file()
    # global mode
    # mode = "export_html"


def import_from_json():
    file_worker.import_from_json_to_csv_file()
    # global mode
    # mode = "import_json"
 

def import_from_html():
    file_worker.import_from_html_to_csv_file()
    # global mode
    # mode = "import_html"


def show_find_data_message(name, lastname, phone, message):
    messagebox.showinfo("Поиск в базе", "Запись успешно найдена???\n" + name + " " + lastname + " " + phone)


def find_data_in_database(name, lastname, phone, additional_form, main_form):

    find_window_empty_message = "Найти данные не получится. Все поля поиска пустые."
    find_window_no_message = "Записи удовлетворяющие условию не найдены."
    find_window_yes_message = ""

    if not data_checker.check_data_empty_all(name.get(), lastname.get(), phone.get()):
        show_add_to_file_message(FIND_WINDOW_HEADER, find_window_empty_message) 
    else:
        lastname_string, name_string, phone_string = data_checker.data_correction(lastname.get(), name.get(), phone.get())
        data_finding = data_finder.find(name_string, lastname_string, phone_string)
        if len(data_finding) == 0:
            show_add_to_file_message(FIND_WINDOW_HEADER, find_window_no_message)
        else:
            find_window_yes_message = f'Найдено {len(data_finding)} записи(ей)\n'
            show_add_to_file_message(FIND_WINDOW_HEADER, find_window_yes_message)
            scrollbar = Scrollbar(main_form)
            scrollbar.pack(side = RIGHT, fill = Y)
    
            data_finding_listbox = Listbox(main_form, yscrollcommand=scrollbar.set, width = 75)
            data_finding_listbox.pack(side = RIGHT, fill = Y)
   
            data_finding_listbox.insert(END, "№  Фамилия               Имя                  Телефон")
            count = 1
            for finding in data_finding:
                data_finding_listbox.insert(END, data_former.format_string(count, finding))
                count += 1
    
            scrollbar.config(command = data_finding_listbox.yview)


        # add_window_message += lastname_string + " " + name_string + " " + phone_string   
        # show_add_to_file_message(ADD_WINDOW_HEADER, add_window_message)

        # name.set("")
        # lastname.set("")
        # phone.set("")
        # form_name.destroy()

    # data_finding = data_finder.find(name.get(), lastname.get(), phone.get())
    # #mode, data = "search", [[lastname.get(), name.get(), "+" + phone.get()]]
    # # show_find_data_message(name.get(), lastname.get(), phone.get())
    # lastname.set(data_fainding[0][0])
    # name.set(data_fainding[0][1])
    # phone.set(data_fainding[0][2])

    # languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
    #          "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
    #          "T-SQL", "PL-SQL", "Typescript"]

    # scrollbar = Scrollbar(main_form)
    # scrollbar.pack(side = RIGHT, fill = Y)
    # #scrollbar.grid(row = 1, column = 2, sticky='nsw') #padx = 0, pady = 0)
    
    # languages_listbox = Listbox(main_form, yscrollcommand=scrollbar.set, width = 75)
    # languages_listbox.pack(side = RIGHT, fill = Y)
   
    
    # for language in languages:
    #     languages_listbox.insert(END, language)
    
    # scrollbar.config(command=languages_listbox.yview)

    # return ""


def find_data_form_info(root):
    find_window = tkinter.Toplevel(root)
    find_window.title("Поиск данных")
    find_window.geometry("280x140")

    name = StringVar()
    lastname = StringVar()
    phone = StringVar()

    name_label = Label(find_window, text = "Введите имя:")
    lastname_label = Label(find_window, text = "Введите фамилию:")
    phone_label = Label(find_window, text = "Введите телефон:")
    plus_label = Label(find_window, text = "+")

    name_label.grid(row = 1, column = 0, sticky = "w")
    lastname_label.grid(row = 3, column = 0, sticky = "w")
    phone_label.grid(row = 5, column = 0, sticky = "w")
    plus_label.grid(row = 5, column = 1, sticky = "e")

    name_input = Entry(find_window, textvariable = name)
    lastname_input = Entry(find_window, textvariable = lastname)
    phone_input = Entry(find_window, textvariable = phone)
 
    name_input.grid(row = 1, column = 2, padx = 5, pady = 5)
    lastname_input.grid(row = 3, column = 2, padx = 5, pady = 5)
    phone_input.grid(row = 5, column = 2, padx = 5, pady = 5)

    #Значения по умолчанию
    name_input.insert(0, "")
    lastname_input.insert(0, "")
    phone_input.insert(0, "")

    message_button = Button(find_window, text = "   Найти   ", command = lambda: find_data_in_database(name , lastname , phone, find_window, root))
    message_button.grid(row = 7, column = 2, padx = 5, pady = 5)

    # languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
    #          "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
    #          "T-SQL", "PL-SQL", "Typescript"]

    # scrollbar = Scrollbar()
    # scrollbar.grid(row = 9, column = 2, sticky='nsw') #padx = 0, pady = 0)
    
    # languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)
    # languages_listbox.grid(row = 9, column = 0, columnspan=2, sticky='nswe')
    
    # for language in languages:
    #     languages_listbox.insert(END, language)
    
    # scrollbar.config(command=languages_listbox.yview)


def show_add_to_file_message(header, message):
    messagebox.showinfo(header, message)


def add_data_to_file(name, lastname, phone, form_name):
    # global mode
    # global data

    # mode, data = "add", [[lastname.get(), name.get(), "+" + phone.get()]]

    add_window_empty_message = "Добавить данные не получится. Не все поля заполнены."
    add_window_message = "Запись успешно добавлена\n"
    if not data_checker.check_data_empty_at_least_one(name.get(), lastname.get(), phone.get()):
        show_add_to_file_message(ADD_WINDOW_HEADER, add_window_empty_message) 
    else:
        lastname_string, name_string, phone_string = data_checker.data_correction(lastname.get(), name.get(), phone.get())
        file_worker.add_to_csv_file([[ lastname_string, name_string, phone_string]])
        add_window_message += lastname_string + " " + name_string + " " + phone_string   
        show_add_to_file_message(ADD_WINDOW_HEADER, add_window_message)

        name.set("")
        lastname.set("")
        phone.set("")
        form_name.destroy()

def add_data_form_info(root):
    add_window = tkinter.Toplevel(root)
    add_window.title("Добавить данные")
    add_window.geometry("280x140")

    name = StringVar()
    lastname = StringVar()
    phone = StringVar()

    name_label = Label(add_window, text = "Введите имя:")
    lastname_label = Label(add_window, text = "Введите фамилию:")
    phone_label = Label(add_window, text = "Введите телефон:")
    plus_label = Label(add_window, text = "+")

    name_label.grid(row = 1, column = 0, sticky = "w")
    lastname_label.grid(row = 3, column = 0, sticky = "w")
    phone_label.grid(row = 5, column = 0, sticky = "w")
    plus_label.grid(row = 5, column = 1, sticky = "e")

    name_input = Entry(add_window, textvariable = name)
    lastname_input = Entry(add_window, textvariable = lastname)
    phone_input = Entry(add_window, textvariable = phone)

    name_input.grid(row = 1, column = 2, padx = 5, pady = 5)
    lastname_input.grid(row = 3, column = 2, padx = 5, pady = 5)
    phone_input.grid(row = 5, column = 2, padx = 5, pady = 5)

    #Значения по умолчанию
    name_input.insert(0, "")
    lastname_input.insert(0, "")
    phone_input.insert(0, "")

    reg_phone = add_window.register(data_checker.check_symbol_phone)
    phone_input.config(validate = "key", validatecommand = (reg_phone, "%P"))

    reg_name_lastname = add_window.register(data_checker.check_symbol_name_lastname)
    lastname_input.config(validate = "key", validatecommand = (reg_name_lastname, "%P"))
    name_input.config(validate = "key", validatecommand = (reg_name_lastname, "%P"))

    message_button = Button(add_window, text = "Добавить", command = lambda: add_data_to_file(name, lastname, phone, add_window))
    message_button.grid(row = 7, column = 2, padx = 5, pady = 5)

def show_all_data(root):
    all_data = file_worker.read_from_csv_file()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side = RIGHT, fill = Y)
    
    data_listbox = Listbox(root, yscrollcommand=scrollbar.set, width = 75)
    data_listbox.pack(side = RIGHT, fill = Y)

    data_listbox.lift()
   
    data_listbox.insert(END, "№  Фамилия               Имя                  Телефон")
    count = 1
    for data in all_data:
        data_listbox.insert(END, data_former.format_string(count, data_former.from_dict_to_value_list(data)))
        count += 1
    
    scrollbar.config(command = data_listbox.yview)


def main_menu():
    root = Tk()
    root.title("Работа с телефонным справочником")
    root.geometry("450x250")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
 
    main_menu = Menu() 
    #find_menu = Menu()
    export_menu = Menu()
    import_menu = Menu()
 
    main_menu.add_cascade(label = "Добавить данные", command = lambda: add_data_form_info(root))
    main_menu.add_cascade(label = "Найти данные", command = lambda: find_data_form_info(root))
    main_menu.add_cascade(label = "Экспорт данных", menu = export_menu)
    main_menu.add_cascade(label = "Импорт данных", menu = import_menu)


    export_menu.add_command(label = "В json формат", command = export_to_json)
    export_menu.add_command(label = "В html формат", command = export_to_html)
    
    import_menu.add_command(label = "Из json формата", command = import_from_json)
    import_menu.add_command(label = "Из html формата", command = import_from_html)

    message_button = Button(text = "Показать все данные",  background="#C0C0C0", command = lambda: show_all_data(root))
    message_button.pack(side = TOP, fill = X)

    root.config(menu = main_menu)
 
    root.mainloop()
 
main_menu()