# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
party_size = int(input("How many people to split the bill? "))

total_bill = bill + bill * (tip * 1 / 100)
individual_cost = total_bill / party_size

print(f"Each person should pay: ${individual_cost:.2f}")