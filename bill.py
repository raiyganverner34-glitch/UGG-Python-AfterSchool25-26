bill = float(input("enter bill amt "))
people = int(input("how many people are sharing the bill"))

tax_rate = 0.0825
tip_rate = .15
tax = bill * tax_rate 
tip = bill * tip_rate
total = bill * tax + tip
per_person = total / people

print("reataurant bill splitter with text & tip") 
