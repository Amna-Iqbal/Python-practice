def divisible_by_five(numbers):
    """Accepts a sequence of CSV binary numbers and returns a string of numbers that are divisible by 5"""
    number = numbers.split(',')
    for n in number:
        n_dec = int(n, 2)
        if n_dec % 5 == 0:
            print(n)


numbers = "0100, 0011, 1010, 1001, 1100, 1001"
divisible_by_five(numbers)
