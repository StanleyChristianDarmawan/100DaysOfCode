print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tipPercent = tip / 100
totalTip = bill * tipPercent
totalBill = bill + totalTip

print(f"Each person should pay: ${round(totalBill/people, 2)}")