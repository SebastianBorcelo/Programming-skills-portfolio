#Eighth excercise

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name = input("Enter the name your looking for: ")

if name in names:
    print(f"{name} is found in the list.")
else:
    print(f"This name isn't on the list")