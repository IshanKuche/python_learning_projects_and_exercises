temperature_in_celsius = float(input("Enter a Temperature you want to convert: "))
converted_temperature_F = temperature_in_celsius * 1.8 + 32
print(f"{temperature_in_celsius}℃ in fahrenheit scale is {converted_temperature_F:.2f}°F")

temperature_in_fahrenheit = float(input("Enter a Temperature you want to convert: "))
converted_temperature_C = (temperature_in_fahrenheit-32) * (5/9)
print(f"{temperature_in_fahrenheit}°F in Celsius scale is {converted_temperature_C:.2f}℃")