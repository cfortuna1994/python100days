print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("whast is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are €5")
        
    elif age <= 18:
        bill = 7
        print("Youth tickets are €7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")       
    else:
        bill = 12
        print("Adult tickets are €12")
        
    photos = input("Would you like a photon taken? Y|N ")
    if photos == "Y":
        print("You have to pay €3")
        bill += 3
       
    print(f"The total bill is: €{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")



'''


#########################################

number = int(input("Which number do you want to check?\n"))

if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")

#################


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
height_final = height ** 2
bmi = weight / height_final

print(bmi)
if bmi < 18.5:
    print(f"your BMI is {bmi} , you are underweight.")
elif bmi < 25:
    print(f"your BMI is {bmi} , you are normal weight.")
elif bmi < 30:
    print(f"your BMI is {bmi} , you are overweight.")
elif bmi < 35:
    print(f"your BMI is {bmi} , you are obese.")
else:
    print(f"your BMI is {bmi} , you are clinically obese.")


year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"Year {year} is a leap year")
elif year % 400 == 0:
    print(f"Year {year} is a leap year")

else:
    print(f"Year {year} is not a leap year")
'''