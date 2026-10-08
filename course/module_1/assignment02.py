print("Welcome to the Tip Calculator and bill splitter!")

bill = float(input("Enter Total Bill Amount: "))
tip = float(input("Enter how much tip u would like to give: "))
people = int(input("Enter number of people: "))

tip_amount = (bill * tip) / 100
total_amount = bill + tip_amount
pp_amount = total_amount / people

print(f"Yr total bill is {total_amount} and yr pp amount is {pp_amount}")
    

