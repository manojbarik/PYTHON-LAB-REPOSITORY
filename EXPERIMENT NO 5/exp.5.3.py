celsius_temps = [0, 20, 30, 37, 100]

fahrenheit_temps = []

for c in celsius_temps:
    f = (c * 9/5) + 32  
    fahrenheit_temps.append(f)

print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)
