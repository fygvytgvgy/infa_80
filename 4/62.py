def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = 60
fahrenheit = 45
print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)} in Fahrenheit")
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)} in Celsius")
