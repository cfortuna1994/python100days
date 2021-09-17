#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("*****Welcome to the tip calculator.******")

total = input("What was the total bill? €") #150.10
tip = input("What percentage tip would you like to give? 10, 12, or 15:\n") #12
people = input ("How many people to split the bill? ") #5

total_as_float = float(total)
tip_as_int = int(tip)
people_as_int = int(people)

Total_final = total_as_float + ( (tip_as_int / 100) * total_as_float )
total_per_person = Total_final / people_as_int
final_amount = round(total_per_person, 2)
final_amount = "{:.2f}".format(total_per_person)
print(f"Each person should pay: €{final_amount}")