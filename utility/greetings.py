from operators.operators_dictionariy_and_list import operators_dictionary


def print_instructions() -> str:
    instructions_text_beginning = "Let's do some Math! This calculator can do " \
                                  "following operations:"
    instructions_text_ending = "Please, if your number is decimal, use '.'"

    operators_with_description = str()
    operations_map = operators_dictionary
    new_line = "" \
               ""
    for key, value in operations_map.items():
        operators_with_description = operators_with_description + key + " -> " + value.description
    return instructions_text_beginning + operators_with_description + instructions_text_ending


def operators_as_strings() -> list:
    operators_as_strings_list = list()
    for key, value in operators_dictionary.items():
        operators_as_strings_list.append(key + " -> " + value.description)
    return operators_as_strings_list
