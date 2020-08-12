def input_validation(first_number, operator, second_number) -> list:
    errors = []
    if first_number is "":
        errors.append("First number is empty!")
    if operator is not "!" and second_number is "":
        errors.append("Second number is empty!")

    return errors
