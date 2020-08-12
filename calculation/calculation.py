from operators.operators_dictionariy_and_list import operators_dictionary
from utility.input_digitalizing import to_number


def calculate(first_number: int or float, operator_symbol: str, second_number: int or float) \
                                                                                               -> int or float or str:
    result = None
    error = None
    operator_checked = operators_dictionary[operator_symbol]

    if operator_symbol == "!":
        second_number = "0"

    try:
        result = operator_checked.calculation(to_number(first_number), to_number(second_number))
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result
