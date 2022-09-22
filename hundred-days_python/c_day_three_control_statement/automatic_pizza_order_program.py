print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

small_pizza = "S"
medium_pizza = "M"
large_pizza = "L"
pepperoni_small = "Y"
pepperoni_m_or_l = 3
cheese = "Y"

bill_small_size_option1 = 15 + 2 + 1
bill_small_size_option2 = 15 + 2
# bill_small_size_option3 = small_pizza + cheese
#
# bill_medium_size_option1 = 20 + pepperoni_m_or_l + cheese
# bill_medium_size_option2 = medium_pizza + pepperoni_m_or_l
# bill_medium_size_option3 = medium_pizza + cheese
#
# bill_large_size_option1 = 25 + pepperoni_m_or_l + cheese
# bill_large_size_option2 = large_pizza + pepperoni_m_or_l
# bill_large_size_option3 = large_pizza + cheese


if small_pizza == "S":
    print(f"Your bill is ${bill_small_size_option1}")
else:
    if pepperoni_small == "Y":
        print(f"Your bill is ${bill_small_size_option2}")
# if medium_pizza == "M":
#     print(f"Your bill is ${bill_medium_size_option1}")
# if large_pizza == "L":
#     print(f"Your bill is ${bill_large_size_option1}")