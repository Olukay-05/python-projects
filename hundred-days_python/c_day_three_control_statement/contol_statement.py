print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

# nested if/else
# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Pay $7")
#     else:
#         print("pay $12")
# else:
#     print("Sorry, you are below the required age")
bill = 0
# if/elif/else
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Pay $5")
    elif age <= 18:
        bill = 7
        print("Pay $7")
    elif age <= 22:
        bill = 12
        print("Pay $12")
    elif age <= 30:
        bill = 15
        print("Pay $15")
    else:
        bill = 20
        print("pay $20")

    wants_photo = input("Do you want photo taken? Y or N")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are below the required age")