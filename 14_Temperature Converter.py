from unittest import result


def celsius_to_fahrenheit(temperature):
    return temperature * 1.8 + 32

def fahrenheit_to_celsius(temperature):
    return (temperature-32) * (5/9)

input_temperature = float(input("Enter a temperature to convert: "))
result1 = celsius_to_fahrenheit(input_temperature)    
result2 = fahrenheit_to_celsius(input_temperature)
print(f"{input_temperature}℃ in fahrenheit scale is {result1:.2f}°F")
print(f"{input_temperature}°F in celsius scale is {result2:.2f}℃")