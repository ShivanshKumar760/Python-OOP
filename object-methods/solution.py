"""
Problem: Object Methods
URL: https://neetcode.io/problems/python-object-methods/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class Pet:class Pet:
    def __init__(self, name: str):    def __init__(self, name: str):
        self.name = name        self.name = name
        self.hunger = 5        self.hunger = 5

    def feed(self):    def feed(self):
        # TODO: Implement this method        # TODO: Implement this method
        # It should decrease the pet's hunger by 1        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet        # and print a message about feeding the pet
        # pass        # pass
        self.hunger-=1        self.hunger-=1
        print("Fluffy has been fed.")        print("Fluffy has been fed.")
        print(f"Fluffy's hunger level: {my_pet.hunger}")        print(f"Fluffy's hunger level: {my_pet.hunger}")

# Create a pet# Create a pet
my_pet = Pet("Fluffy")my_pet = Pet("Fluffy")

# TODO: Feed the pet three # TODO: Feed the pet three 
for i in range(3):for i in range(3):
    my_pet.feed()    my_pet.feed()
