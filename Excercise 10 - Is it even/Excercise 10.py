#Tenth excercise

def check_if (nmbr):
    if nmbr % 2 == 0:
        return f'The number {nmbr} is even.'
    else:
        return f'The number {nmbr} is odd.'
    

def main():
    nmbr = int(input("Please enter a number: "))
    print(check_if(nmbr))

if __name__ == "__main__":
    main()