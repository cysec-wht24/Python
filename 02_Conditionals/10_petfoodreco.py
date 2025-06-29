animal_type = "dog"
animal_age = 1

if animal_type == "dog" and animal_age < 2:
    menu = "puppy food"
elif animal_type == "cat" and animal_age > 5:
    menu = "senior cat food"
else:
    menu = "eat whatever available"

print(menu)