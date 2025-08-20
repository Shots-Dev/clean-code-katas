#Task 7

temp = 325

def fahrenheit_to_celsius(temp):
    celsius = round(((temp - 32) * (5 / 9)),2)

    print(celsius)

def celsius_to_fahrenheit(temp):
    celsius = round(((temp * 1.8) + 32),2)

    print(celsius)

fahrenheit_to_celsius(temp)
celsius_to_fahrenheit(temp)