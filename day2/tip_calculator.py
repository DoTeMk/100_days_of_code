#Day 2 Final Project - 11_06_24

print("Welcome to tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? "))
split_number = int(input("How many people to split the bill? "))

bill_splited = (total_bill + (total_bill * (tip_percentage / 100))) / split_number
print(f"Each person should pay: ${bill_splited:.2f}")