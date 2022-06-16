
def format_string(number, data_list):
    length_number = 5
    length_item = 20
    result = str(number) + " " * (length_number - len(str(number)))
    for item in data_list:
        result += item + " " * (length_item - len(str(item)))
    return result


def from_dict_to_value_list(dict):
    return [dict['Lastname'], dict['Name'], dict['Phone']]