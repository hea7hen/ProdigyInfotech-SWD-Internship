def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == "celsius" or unit == "c":
        print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F = {celsius_to_kelvin(value):.2f}K")
    elif unit == "fahrenheit" or unit == "f":
        print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C = {fahrenheit_to_kelvin(value):.2f}K")
    elif unit == "kelvin" or unit == "k":
        print(f"{value}K = {kelvin_to_celsius(value):.2f}°C = {kelvin_to_fahrenheit(value):.2f}°F")
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

value = float(input("Enter temperature value: "))
unit = input("Enter unit (Celsius, Fahrenheit, Kelvin): ")
convert_temperature(value, unit)
