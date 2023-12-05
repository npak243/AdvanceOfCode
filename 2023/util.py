def parse_first_last_digit(input_str):
    """Parse the first/last digit"""
    first_digit = 0
    last_digit = 0
    for char in input_str:
        if char >= '0' and char <= '9':
            first_digit = int(char)*10
            break
    for char in input_str.reverse():
        if char >= '0' and char <= '9':
            last_digit = int(char)
            break

    return first_digit + last_digit
