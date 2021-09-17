# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

liveuntil = 90
restoflive = 90 - int(age)
days = restoflive * 365
weeks = restoflive * 52
months = restoflive * 12

print(f"You have {days}, {weeks} weeks, and {months} months left.")
