def input_validation(first_number, operator, second_number) -> list:
    errors = []
    if first_number is "":
        errors.append("First number is empty!")
    if operator != "!" and operator != "lg" and operator != "ln" and second_number is "":
        errors.append("Second number is empty!")

    return errors
