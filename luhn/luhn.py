"""Calculate checksum digit from any given number using Luhn algorithm."""


def create_luhn_checksum(number):
    """
    Generates luhn checksum from any given integer number.
    :param number: Number input. Any integer number.
    :return: Calculated checksum digit
    """
    str_number = str(number)
    n_digits = len(str_number)
    parity = n_digits % 2
    sum_n = 0
    # Loop over digits, start at most right hand point
    for index in range(n_digits, 0, -1):
        digit = int(str_number[index - 1])
        if parity == index % 2:
            digit += digit
        if digit > 9:
            digit -= 9
        sum_n += digit
    return (sum_n * 9) % 10


def verify_checksum(number_plus_cs):
    """
    Verify a given number that includes a Luhn checksum digit.
    :param number_plus_cs: A number + appended checksum digit.
    :return: True if verification was successful, false if not.
    """
    number = str(number_plus_cs)[:-1]
    checksum = number_plus_cs % 10
    if create_luhn_checksum(number) is not checksum:
        return False
    else:
        return True
