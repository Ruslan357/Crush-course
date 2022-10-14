favorite_numbers = {'Ruslan': [3, 6, 4, 8, 5],
                    'Dima': [5, 2, 6, 1],
                    'Yana': [3, 1, 7, 5, 4],
                    'Bogdan': [9, 1, 5, 2]}

for name,numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite nambers are: ",end='')
    for number in numbers:
        print(f'{number} ',end='')
    print()
