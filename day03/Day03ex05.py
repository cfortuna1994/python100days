print("Welcome To Love Calculator ❤ :")

name1 = str(input("Enter Your Name:"))
name2 = str(input("Enter Your Partner Name:"))

#True love
print(name1,name2)

name1_lower = name1.lower()
name2_lower = name2.lower()

combined_name = name1.lower() +  name2.lower()

t = combined_name.count("t") 
r = combined_name.count("r")
u = combined_name.count("u") 
e = combined_name.count("e") 
True_total = t + r + u + e
l = combined_name.count("l")  
o = combined_name.count("o")  
v = combined_name.count("v")  
e = combined_name.count("e") 
love_total = l + o + v + e

total =  int(str(True_total) + str(love_total))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 or total <= 50:
     print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")