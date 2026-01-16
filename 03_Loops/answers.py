print("01 Count positive No.")

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of Positive number is: ", positive_number_count)

print("------------------------------")

print("02 Sum of even no.")
n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number is: , ", sum_even)

print("------------------------------")

print("03 Mult table")

number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)

print("------------------------------")

print("04 Reverse String")
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)
print("------------------------------")

print("05 Find 1st non repeated char")
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
print("------------------------------")

print("06 Factorial calci")
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)

print("------------------------------")

print("07 Validate input")
while True:
    value = int(input("Please enter number between 1 and 10: "))
    if 1 <= value <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Input")

print("------------------------------")

print("08 Prime no. checker")
number = 29

is_prime = True

if number > 1:
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break

print(is_prime)

print("------------------------------")

print("09 unique list check")
items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate: ", item)
        break
    unique_items.add(item)

print("------------------------------")

print("10 exponential backoff")
# this strategy used during password reset, during sending otp
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
