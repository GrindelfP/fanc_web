from operators.operators_lists import operators_regex_list, operators_list


def to_number(number_as_text: str) -> int or float:
    if "." in number_as_text:
        number_as_digit = float(number_as_text)
    else:
        number_as_digit = int(number_as_text)

    return number_as_digit


def calculate(first_number: int or float, operator_symbol: str, second_number: int or float) \
                                                                                               -> int or float or str:
    result = None
    error = None
    operator_checked = operators_list[operator_symbol]

    try:
        result = operator_checked.calculation(to_number(first_number), to_number(second_number))
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result
