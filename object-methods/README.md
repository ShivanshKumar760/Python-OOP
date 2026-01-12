# Object Methods

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-object-methods/question)

---

## 📋 Problem Description

Methods are functions that belong to a class or object. They define the behavior of the class or object.

Defining methods in a classLet's update our SuperHero class to include two methods, use_power() and take_damage(amount):

We can create an object of the SuperHero class and call the methods on it:

Let's break down what's happening in this code: The use_power() method: Takes no parameters (except self, which we'll explain in a future lesson).

Prints a message saying the superhero is using their power. The take_damage(amount) method: Takes a parameter amount and subtracts it from the object's health.

Prints a message about the damage taken and the object's new health. Methods are called on an object using dot notation, like iron_man.use_power(). If a method takes parameters, they are passed in the same way as function arguments e.g. iron_man.take_damage(20).

ChallengePlease see the starter code of the Pet class and complete the following in the feed method: Decrease the pet's hunger by 1

Print the string 'Fluffy has been fed.'.

Print the current hunger level of my_pet, in this format: 'Fluffy's hunger level: X' And then call the feed method three times on my_pet.

After completing the task your code should give the following expected output.

Expected Output Method vs Function

Methods are just functions that are defined inside a class. A function defined outside of a class is not a method.

---

## 💡 Solution

Check the `solution.py` file in this directory for the complete implementation.

---

## 📊 Complexity Analysis

*Add your complexity analysis here after solving*

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

<sub>This problem was automatically synced from NeetCode using [NeetCode GitHub Pusher](https://github.com/)</sub>
