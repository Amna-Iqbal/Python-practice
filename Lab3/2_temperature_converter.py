def celsius_to_farhrenheit(celsius):
    """Takes temperature in celsius and converts to Fahrenheit"""
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

def farhrenheit_to_celsius(fahrenheit):
    """Takes temperature in fahrenheit and converts to celsius """
    #f = (c * 9/5) + 32
    celsius = (fahrenheit - 32) * 5/9
    return celsius

x = farhrenheit_to_celsius(45)
print(f"Fahrenheit to Celsius: {x}")
y = celsius_to_farhrenheit(7)
print(f"Celsius to Fahrenheit: {y}")
