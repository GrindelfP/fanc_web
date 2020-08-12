def to_number(number_as_text: str) -> int or float:
    """

    :rtype: object
    """
    if "." in number_as_text:
        number_as_digit = float(number_as_text)
    else:
        number_as_digit = int(number_as_text)

    return number_as_digit
