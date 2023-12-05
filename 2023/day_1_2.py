def parse_first_last_digit(input_str: str):
    """Parse the first/last digit"""
    check_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    convert_str_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    first_digit = None
    pos_1 = 100
    last_digit = None
    pos_2 = -100
    for digit in check_list:
        cur_pos = input_str.find(digit)
        if cur_pos >= 0 and cur_pos < pos_1:
            pos_1 = cur_pos
            first_digit = convert_str_int[digit]

        cur_pos = input_str.rfind(digit)
        if cur_pos >= 0 and cur_pos > pos_2:
            pos_2 = cur_pos
            last_digit = convert_str_int[digit]

    return first_digit*10 + last_digit

result = 0  # result = 54540
# ifile = open("day_1_input_test.txt", mode="r", encoding="utf-8")
ifile = open("day_1_input.txt", mode="r", encoding="utf-8")
for line in ifile:
    result += parse_first_last_digit(line)
ifile.close()

print(result)
