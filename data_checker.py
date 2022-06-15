def delete_extra_spaces(string_original):
    string_original = string_original.strip()
    return string_original

def check_symbol_phone(symbol):
    if symbol.isdigit() or symbol == "":
        return True
    else:
        return False

def check_symbol_name_lastname(symbol):
    if symbol.isalpha() or symbol == "":
        return True
    else:
        return False