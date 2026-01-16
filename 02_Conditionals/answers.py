print("01 age gp")
my_age = 65

if my_age < 13:
    print("Child")
elif my_age < 20:
    print("Teenager")
elif my_age < 60:
    print("Adult")
else:
    print("Senior")

print("------------------------------")

print("02 movie ticket")
age =  25
day = "Wednesday"

price = 12 if age >= 18 else 8
print(f"price: {price}")

if(day == "Wednesday"):
    print("Today is discount for 2%")
    print(f"Price for person with age {age} on Wednesday is {0.98 * price}")

print("------------------------------")

print("03 grade calci")
score = 98

if score >= 101:
    print("Please verify your grade again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)

print("------------------------------")

print("04 Ripe Checker")
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")

print("------------------------------")

print("05 weather suggestions")
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)

print("------------------------------")

print("06 transport selection")
distance =  12

if distance < 3:
    print("Walk")
elif distance > 15:
    print("Car")
else:
    print("Bike")


# if distance < 3:
#     print("Walk")
# else:
#     if distance > 15:
#         print("Car")
#     else:
#         print("Bike") 

print("------------------------------")

print("07 coffee customer")
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee  = order_size + " with an extra shot coffee"
else:
    coffee = order_size + " coffee"

print(coffee)

print("------------------------------")

print("08 password checker")
password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)

print("------------------------------")

print("09 leap checker")
year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}: Leap year")
else: 
    print(f"{year}: Not Leap Year")

print("------------------------------")

print("10 pet food reco")
animal_type = "dog"
animal_age = 1

if animal_type == "dog" and animal_age < 2:
    menu = "puppy food"
elif animal_type == "cat" and animal_age > 5:
    menu = "senior cat food"
else:
    menu = "eat whatever available"

print(menu)