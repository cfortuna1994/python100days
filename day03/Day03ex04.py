'''
#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
print("WElcome to the pizzaria Fortunato")

bill = 0
size_pizza = input("Which size of pizza would you like?  Small Pizza: $15 \
Medium Pizza: $20 \
Large Pizza: $25 \
(S/M/L): ")

if size_pizza == "S":
    bill += 15
    print("You've got the small pizza size.")

elif size_pizza == "M":
    bill += 20
    print("You've got the Medium pizza size.")

elif size_pizza == "L":
    bill += 25
    print("You've got the Large pizza size.")

else:
    print("Invalid size")

Pepperoni = input("Would you like to add pepperoni? (Y|N) ")
if Pepperoni == "Y":
    if size_pizza == "S":
        bill += 2
    else:
        bill += 3
Extra_cheese = input("Would you like extra cheese?  (Y|N)  ")
if Extra_cheese:
    bill += 1

print(f"Your total bill is €{bill}")
