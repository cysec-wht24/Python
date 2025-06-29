age =  25
day = "Wednesday"

price = 12 if age >= 18 else 8
print(f"price: {price}")

if(day == "Wednesday"):
    print("Today is discount for 2%")
    print(f"Price for person with age {age} on Wednesday is {0.98 * price}")
