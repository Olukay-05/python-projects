height = eval(input("Enter your height in m: "))
weight = eval(input("Enter your weight in kg: "))
bmi = weight / height ** 2
bmi_as_int = int(bmi)
print("Your bmi is: ", bmi_as_int)
