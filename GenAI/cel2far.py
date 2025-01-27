
def cel_to_fah(celsious_temp):
	return celsious_temp * 1.8 + 32

celsious_temp = float(input("Enter Celcious temprature : "))
fahrenheit_temp = cel_to_fah(celsious_temp)

print(f"{celsious_temp}°C is equal to {fahrenheit_temp}")

