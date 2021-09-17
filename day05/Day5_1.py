'''
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

len()
sum()

'''

student_heights = input("Input a list of student heights").split()
print(student_heights)
qty_list = 0
total_student_heights = 0

for n in student_heights:
    qty_list += 1
    print(n)
    total_student_heights += int(n)

media = total_student_heights/qty_list

print(media)