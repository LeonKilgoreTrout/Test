def sum_numbers(number: int) -> int:
    sum_of_digits = 0
    while number // 10:
        sum_of_digits += number % 10
        number = number // 10
    else:
        sum_of_digits += number
    return sum_of_digits
