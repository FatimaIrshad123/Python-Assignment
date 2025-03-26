def fahrenheit_to_celsius():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temprature: {degrees_fahrenheit}F = {degrees_celsius}")

fahrenheit_to_celsius()