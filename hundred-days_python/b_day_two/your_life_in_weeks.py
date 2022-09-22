age = input("What is your current age?  ")
target_age = 90

number_of_years_left = 90 - int(age)
number_of_months_left = number_of_years_left * 12
number_of_weeks_left = number_of_years_left * 52
number_of_days_left = number_of_years_left * 365
actual_value = f"you have {number_of_days_left} days, {number_of_weeks_left} weeks, and {number_of_months_left} months"
print(actual_value)
                