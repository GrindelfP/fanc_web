from operators.operators_dictionariy_and_list import operators_dictionary
from utility.input_digitalizing import to_number


def calculate(first_number: int or float, operator_symbol: str, second_number: int or float) \
                                                                                     -> int or float or str:
    first_number_as_digit = to_number(first_number)
    second_number_as_digit = None
    if second_number is not "":
        second_number_as_digit = to_number(second_number)
    result = None
    error = None
    operator_checked = operators_dictionary[operator_symbol]

    try:
        result = operator_checked.calculation(first_number_as_digit, second_number_as_digit)
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result
