temp = int(input("Enter tempreture:"))
if temp <=20:
    print("Status:cold")
elif temp <=35:
    print("Status:Normal")
else:
    print("Status:Hot")

calsius = int(input("Enter the temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("The celsius degree in fahrenheit is:",fahrenheit)