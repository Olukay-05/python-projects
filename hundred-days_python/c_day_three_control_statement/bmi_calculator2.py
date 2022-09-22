height = eval(input("Enter your height in m: "))
weight = eval(input("Enter your weight in kg: "))
bmi = weight / height ** 2
bmi = round(float(bmi), 2)

# if bmi < 18.5:
#     print("You are underweight")
#     if bmi >= 18.5:
#         print("normal weight")
#     elif bmi <= 25:
#         print("normal weight")
#     elif bmi <= 30:
#         print("overweight")
#     elif bmi <= 35:
#         print("obese")
# else:
#     print("You are clinically obese")

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi <= 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi <= 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi <= 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")





