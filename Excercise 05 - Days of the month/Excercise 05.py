#Fifth Excercise

days_of_the_months = {
    1: 31,  # January
    2: 28,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31  # December
}


Month =int(input("Please enter a number 1-12 for a month"))

if Month == 2:
    leap_year = input('is it a leap year?: ')
    while True:
        if leap_year =='yes':
            days_of_the_months[2] = 29
            break
        elif leap_year =='no':
            days_of_the_months[2] = 28
        else:
            leap_year = input("Please enter the choicecs either yes or no: ")

if Month in days_of_the_months:
    print(f'The number of days on {Month} is {days_of_the_months[Month]}')
else:
    print(" You have to enter a number between 1 - 12")
       