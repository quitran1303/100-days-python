print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people do you want to split the bill?"))
each_person = total_bill*(1+percent/100)/people
print(f"Each person should pay: $ {round(each_person,2)}")