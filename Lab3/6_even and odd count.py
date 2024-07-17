def count_even_numbers(series):
    """Counts even numbers in a series of numbers"""
    even_number=0
    odd_number=0
    for number in series:
        if number%2==0:
            even_number+=1
        else:
            odd_number +=1
    return even_number, odd_number



number_series =(1, 2, 3, 4, 5, 6, 7, 8, 9)  
x, y = count_even_numbers(number_series)
print(f"No of even numbers: {x}")
print(f"No of odd numbers: {y}")
