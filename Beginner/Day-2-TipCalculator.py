print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $ "))
tipPercentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
totalPeople = int(input("How many people to split the bill?" ))
totalTip = totalBill * (tipPercentage/100)
eachPersonPay = (totalBill + totalTip) / totalPeople

print(f"Each person should pay: ${round(eachPersonPay, 2)}")