"""
Day 2 - Tip Calculator
Calculate each person's share of a restaurant bill, including tip,
split across a number of people.
"""

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people

# Round to 2 decimal places
bill_per_person = round(bill_per_person, 2)

print(f"Each person should pay: ${bill_per_person}")
