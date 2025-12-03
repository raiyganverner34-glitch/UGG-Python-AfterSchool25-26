# program Description: calcuates bill

#Asking user for bill amt 

bill = float(input("enter bill amt: "))

# Asking user for no. of people 
people = int (input("enter no. of people sharing the bill: "))


#Define tax and tip rates 

tax_rate = 0.0825
tip_rate = 0.15

#Formula to calculate ate tax, tip and total 
tax = bill * tax_rate

tip = bill * tip_rate

total = bill * tip_rate 

#calulate amt each person owes
per_person = total / people 

#printing everything 
print("restaurant bill calculate")
print("_ _ _ _ _ _ _ _ _ _ _ _ _")
print(f"original bill:  {bill}")
print(f"sales Tax: {tax}" )
print(f"tip 15% {tip}")
print(f"here is the total bill {total}")
print(f"each person's share {per_person}")
