while True:
    value = int(input("Please enter number between 1 and 10: "))
    if 1 <= value <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Input")