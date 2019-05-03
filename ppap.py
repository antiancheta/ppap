import random

random_fruits = ["apple","banana","cherry","eggplant","strawberry","watermelon","mango"]
random_writing_utensils = ["pencil","pen","quill","crayon","marker","paintbrush"]

fruit = random.choice(random_fruits)
utensil = random.choice(random_writing_utensils)
fruit2 = random.choice(random_fruits)

print("I have a " + utensil + ", I have a " + fruit)
print("\nU h\n")
print(fruit + " " + utensil)
print("\nI have a " + utensil +", I have a " + fruit2)
print("\nU h\n")
print(fruit2 + " " + utensil)
print("\n" + fruit + " " + utensil)
print("\n" + fruit2 + " " + utensil)
print("\nU h\n")
print(utensil + " " + fruit2 + " " + fruit + " " + utensil)
