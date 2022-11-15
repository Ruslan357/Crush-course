while True:
    age = int(input('Please enter your age '))
    if age < 3:
        print('The ticket is free of charge')
    elif age >= 3 and age <= 12:
        print('Ticket price is $10')
    elif age >= 12:
        print('Ticket price is $15')
