# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# Functions with multiple inputs

def greet_multiple_people(person1, person2):
    print(f"Hello {person1}!")
    print(f"My name is {person2}")

greet_multiple_people("Angela", "Sabeen")


# Keyword Arguments

def greet_location(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}")

greet_location(location="Munich", name="Sabeen")