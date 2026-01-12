"""
Problem: Object Attributes
URL: https://neetcode.io/problems/python-object-attributes/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class Pet:class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name        self.name = name
        self.species = species        self.species = species
        self.hunger = hunger        self.hunger = hunger
        self.energy = energy        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes# TODO: Print Whiskers' initial attributes
print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
# TODO: Modify Whiskers' attributes:# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3#  - Decrease hunger by 3
#  - Increase energy by 2#  - Increase energy by 2
whiskers.hunger=whiskers.hunger-3whiskers.hunger=whiskers.hunger-3
whiskers.energy=whiskers.energy+2whiskers.energy=whiskers.energy+2

# TODO: Print Whiskers' modified attributes# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
