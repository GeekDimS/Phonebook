import data_checker
from tkinter import *
from tkinter import messagebox

def export_to_json():
    #Здесь вызвать функцию экспорта в json
    return "export_to_json"


def export_to_html():
    #Здесь вызвать функцию экспорта в html
    return "export_to_html"

def show_find_data_message(name, lastname, phone):
    messagebox.showinfo("Поиск в базе", "Запись успешно найдена???\n" + name + " " + lastname + " " + phone)

def find_data_in_database(name, lastname, phone):
    #Удаляем экстра пробелы в начале и конце введенных данных
    # data_checker.delete_extra_spaces(name)
    # data_checker.delete_extra_spaces(lastname)
    # data_checker.delete_extra_spaces(phone)

    show_find_data_message(name.get(), lastname.get(), phone.get())
    name.set("")
    lastname.set("")
    phone.set("")
    #!!!!!!!Можно здесь вызвать функцию поиска
    return ""

def find_data_form_info():
    name = StringVar()
    lastname = StringVar()
    phone = StringVar()

    name_label = Label(text = "Введите имя:")
    lastname_label = Label(text = "Введите фамилию:")
    phone_label = Label(text = "Введите телефон:")

    name_label.grid(row = 1, column = 0, sticky = "w")
    lastname_label.grid(row = 3, column = 0, sticky = "w")
    phone_label.grid(row = 5, column = 0, sticky = "w")

    name_input = Entry(textvariable = name)
    lastname_input = Entry(textvariable = lastname)
    phone_input = Entry(textvariable = phone)
 
    name_input.grid(row = 1, column = 2, padx = 5, pady = 5)
    lastname_input.grid(row = 3, column = 2, padx = 5, pady = 5)
    phone_input.grid(row = 5, column = 2, padx = 5, pady = 5)

    message_button = Button(text = "   Найти   ", command = lambda: find_data_in_database(name, lastname, phone))
    message_button.grid(row = 7, column = 2, padx = 5, pady = 5)

def show_add_to_file_message(name, lastname, phone):
    messagebox.showinfo("Добавление в базу", "Запись успешно добавлена\n" + name + " " + lastname + " " + phone)


def add_data_to_file(name, lastname, phone):
    #Удаляем экстра пробелы в начале и конце введенных данных
    # data_checker.delete_extra_spaces(name)
    # data_checker.delete_extra_spaces(lastname)
    # data_checker.delete_extra_spaces(phone)

    show_add_to_file_message(name.get(), lastname.get(), phone.get())
    name.set("")
    lastname.set("")
    phone.set("")
    #!!!!!!!Можно здесь вызвать функцию добавления в файл
    return ""


def add_data_form_info():
    name = StringVar()
    lastname = StringVar()
    phone = StringVar()

    name_label = Label(text = "Введите имя:")
    lastname_label = Label(text = "Введите фамилию:")
    phone_label = Label(text = "Введите телефон:")

    name_label.grid(row = 1, column = 0, sticky = "w")
    lastname_label.grid(row = 3, column = 0, sticky = "w")
    phone_label.grid(row = 5, column = 0, sticky = "w")

    name_input = Entry(textvariable = name)
    lastname_input = Entry(textvariable = lastname)
    phone_input = Entry(textvariable = phone)
 
    name_input.grid(row = 1, column = 2, padx = 5, pady = 5)
    lastname_input.grid(row = 3, column = 2, padx = 5, pady = 5)
    phone_input.grid(row = 5, column = 2, padx = 5, pady = 5)

    message_button = Button(text = "Добавить", command = lambda: add_data_to_file(name, lastname, phone))
    message_button.grid(row = 7, column = 2, padx = 5, pady = 5)


def main_menu():
    root = Tk()
    root.title("Работа с телефонным справочником")
    root.geometry("400x150")
 
    main_menu = Menu() 
    #find_menu = Menu()
    export_menu = Menu()
 
    main_menu.add_cascade(label="Добавить данные", command = add_data_form_info)
    main_menu.add_cascade(label="Найти данные",command = find_data_form_info)
    main_menu.add_cascade(label="Экспортировать данные в", menu = export_menu)

    export_menu.add_command(label = "В json формат", command = export_to_json)
    export_menu.add_command(label = "В html формат", command = export_to_html)


    root.config(menu = main_menu)
 
    root.mainloop()

main_menu()