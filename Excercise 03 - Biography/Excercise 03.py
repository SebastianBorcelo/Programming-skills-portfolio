#Third excercise

name = (input("Enter your name: "))

hometown = (input("Enter your hometown: "))

try: 
  age = int(input("Enter your age: "))
except ValueError:
  print("You must enter a number for your age")


Biography = {
  'Name': name,
  'Hometown': hometown,
  'Age': age,
}

print(f"My Name is: {Biography['Name']}\nMy Hometown is: {Biography['Hometown']}\nMy Age is: {Biography['Age']}")