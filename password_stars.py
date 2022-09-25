"""
Get a password with minimum length and display asterisks
"""

min_length = 6


def main():
    password = get_password(min_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Please enter password of at least {} characters: ".format(min_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Please enter password of at least {} characters: ".format(min_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()