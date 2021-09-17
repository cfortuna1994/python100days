# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
'''
def greet():
    print("statement 1")
    print("statement 2")
    print("statement 3")

greet()

def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How do you do {name}")

greet_with_name("Christian")
'''

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")
