from operators.operators_dictionariy_and_list import operators_dictionary


def print_operators_dict() -> str:
    operators_with_description = str()
    for key, value in operators_dictionary.items():
        operators_with_description = operators_with_description + key + " -> " + value.description
    return operators_with_description


def operators_as_strings() -> list:
    operators_as_strings_list = list()
    for key, value in operators_dictionary.items():
        operators_as_strings_list.append(key + " -> " + value.description)
    return operators_as_strings_list
