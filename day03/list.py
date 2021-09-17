import random
states_of_america = ["Delaware", "Penn"]

names = "Angela, Ben, Jenny, Michael, Chloe"

name = names.split(", ")

print(name)
number_of_elements = len(name)

index = random.randint(0, number_of_elements - 1)

print(name[index])