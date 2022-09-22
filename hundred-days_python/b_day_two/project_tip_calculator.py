print("Welcome to the tip calculator!\n")
total_bill = (eval(input("What was the total bill? $")))
discount = (eval(input("What percentage tip would you like to give? 10, 12, 0r 15? ")))
number_of_people = (eval(input("How many people to split the bill? ")))

percentage_tip = total_bill * (discount / 100)
total_bill += percentage_tip

amount_each_person_pay = round(total_bill / number_of_people, 2)
print("Each person should pay: $", amount_each_person_pay)
