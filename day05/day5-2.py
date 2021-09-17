student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest = 0
for score in student_scores:
    if(score > highest):
        highest = score


print(f"The highest score in the class is: {highest}")

i = 0

for x in range(1,101):
    if x % 2 == 0:
        i += x

print(i)