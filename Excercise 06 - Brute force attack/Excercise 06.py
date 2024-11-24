#Sixth exercise

password =("12345")

code  = False
while code == False:
    inputpassword = input("Enter your password")
    if inputpassword == password:
        print ("Access granted")
        code = True

    else:
        print("Input password, Acess denied")