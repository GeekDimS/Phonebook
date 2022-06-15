import data_checker
import data_finder
import file_worker
import tkinter
from tkinter import *
from tkinter import messagebox

mode = ""
data = [[]]

def export_to_json():
    global mode
    mode = "export_json"


def export_to_html():
    global mode
    mode = "export_html"


def import_from_json():
    global mode
    mode = "import_json"
 

def import_from_html():
    global mode
    mode = "import_html"


def show_find_data_message(name, lastname, phone):
    messagebox.showinfo("Поиск в базе", "Запись успешно найдена???\n" + name + " " + lastname + " " + phone)


def find_data_in_database(name, lastname, phone):

    data_fainding = data_finder.find(name.get(), lastname.get(), phone.get())
    #mode, data = "search", [[lastname.get(), name.get(), "+" + phone.get()]]
    # show_find_data_message(name.get(), lastname.get(), phone.get())
    lastname.set(data_fainding[0][0])
    name.set(data_fainding[0][1])
    phone.set(data_fainding[0][2])


def find_data_form_info():
    name = StringVar()
    lastname = StringVar()
    phone = StringVar()

    name_label = Label(text = "Введите имя:")
    lastname_label = Label(text = "Введите фамилию:")
    phone_label = Label(text = "Введите телефон:")
    plus_label = Label(text = "+")

    name_label.grid(row = 1, column = 0, sticky = "w")
    lastname_label.grid(row = 3, column = 0, sticky = "w")
    phone_label.grid(row = 5, column = 0, sticky = "w")

    name_input = Entry(textvariable = name)
    lastname_input = Entry(textvariable = lastname)
    phone_input = Entry(textvariable = phone)
    plus_label.grid(row = 5, column = 1, sticky = "e")
 
    name_input.grid(row = 1, column = 2, padx = 5, pady = 5)
    lastname_input.grid(row = 3, column = 2, padx = 5, pady = 5)
    phone_input.grid(row = 5, column = 2, padx = 5, pady = 5)

    #Значения по умолчанию
    name_input.insert(0, "")
    lastname_input.insert(0, "")
    phone_input.insert(0, "")

    languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

    scrollbar = Scrollbar()
    scrollbar.grid(row = 9, column = 2, sticky='nsw') #padx = 0, pady = 0)
    
    languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)
    languages_listbox.grid(row = 9, column = 0, columnspan=2, sticky='nswe')
    
    for language in languages:
        languages_listbox.insert(END, language)
    
    scrollbar.config(command=languages_listbox.yview)

    message_button = Button(text = "   Найти   ", command = lambda: find_data_in_database(name , lastname , phone))
    message_button.grid(row = 7, column = 2, padx = 5, pady = 5)

def show_add_to_file_message(name, lastname, phone):
    messagebox.showinfo("Добавление в базу", "Запись успешно добавлена\n" + name + " " + lastname + " " + phone)


def add_data_to_file(name, lastname, phone, form_name):
    global mode
    global data

    mode, data = "add", [[lastname.get(), name.get(), "+" + phone.get()]]
    show_add_to_file_message(name.get(), lastname.get(), phone.get())
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

# def add_data_form_info():

#     name = StringVar()
#     lastname = StringVar()
#     phone = StringVar()

#     name_label = Label(text = "Введите имя:")
#     lastname_label = Label(text = "Введите фамилию:")
#     phone_label = Label(text = "Введите телефон:")
#     plus_label = Label(text = "+")

#     name_label.grid(row = 1, column = 0, sticky = "w")
#     lastname_label.grid(row = 3, column = 0, sticky = "w")
#     phone_label.grid(row = 5, column = 0, sticky = "w")
#     plus_label.grid(row = 5, column = 1, sticky = "e")

#     name_input = Entry(textvariable = name)
#     lastname_input = Entry(textvariable = lastname)
#     phone_input = Entry(textvariable = phone)

#     name_input.grid(row = 1, column = 2, padx = 5, pady = 5)
#     lastname_input.grid(row = 3, column = 2, padx = 5, pady = 5)
#     phone_input.grid(row = 5, column = 2, padx = 5, pady = 5)

#     #Значения по умолчанию
#     name_input.insert(0, "Илья")
#     lastname_input.insert(0, "Кошкин")
#     phone_input.insert(0, "4768888888")

#     # reg_phone = .register(data_checker.check_phone)


#     message_button = Button(text = "Добавить", command = lambda: add_data_to_file(name, lastname, phone))
#     message_button.grid(row = 7, column = 2, padx = 5, pady = 5)


def main_menu():
    root = Tk()
    root.title("Работа с телефонным справочником")
    root.geometry("450x150")
 
    main_menu = Menu() 
    #find_menu = Menu()
    export_menu = Menu()
    import_menu = Menu()
 
    main_menu.add_cascade(label = "Добавить данные", command = lambda: add_data_form_info(root))
    main_menu.add_cascade(label = "Найти данные",command = find_data_form_info)
    main_menu.add_cascade(label = "Экспорт данных", menu = export_menu)
    main_menu.add_cascade(label = "Импорт данных", menu = import_menu)


    export_menu.add_command(label = "В json формат", command = export_to_json)
    export_menu.add_command(label = "В html формат", command = export_to_html)
    
    import_menu.add_command(label = "Из json формата", command = import_from_json)
    import_menu.add_command(label = "Из html формата", command = import_from_html)


    root.config(menu = main_menu)
 
    root.mainloop()

main_menu()